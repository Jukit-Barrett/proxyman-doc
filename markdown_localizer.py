#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, Optional, Tuple
from urllib.parse import urlparse, unquote

import requests

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}


@dataclass
class MdImageLocalizeConfig:
    images_dir_name: str = "images"
    timeout_seconds: int = 30
    dry_run: bool = False
    in_place: bool = False
    output_md_path: Optional[str] = None  # 如果设置，则忽略 in_place
    fix_alt_media_backslash: bool = False  # 开关：alt=media\ -> alt=media


@dataclass
class MdImageLocalizeResult:
    input_md: str
    output_md: str
    images_dir: str
    replaced_map: Dict[str, str]  # 本地相对路径
    failed_map: Dict[str, str]  # 失败原因


def setup_logger(name: str = "md_image_localizer", level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        fmt = logging.Formatter("[%(levelname)s] %(message)s")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger


def is_http_url(s: str) -> bool:
    return s.startswith("http://") or s.startswith("https://")


def normalize_url(url: str, fix_alt_media_backslash: bool) -> str:
    """
    可选策略：把 'alt=media\\' 替换成 'alt=media'
    """
    if not fix_alt_media_backslash:
        return url
    return url.replace("alt=media\\", "alt=media")


def guess_ext_from_url(url: str) -> Optional[str]:
    try:
        parsed = urlparse(url)
        path = unquote(parsed.path or "")
        ext = Path(path).suffix.lower()
        if ext in IMAGE_EXTS:
            return ext
    except Exception:
        pass
    return None


def sanitize_filename(name: str) -> str:
    name = name.strip()
    name = re.sub(r"[^\w.\-]+", "_", name, flags=re.UNICODE)
    return name or "image"


def stable_name_from_url(url: str, fallback_ext: str) -> str:
    parsed = urlparse(url)
    path = unquote(parsed.path or "")
    base = Path(path).name or "image"
    base_no_ext = Path(base).stem or "image"
    base_no_ext = sanitize_filename(base_no_ext)

    h = hashlib.sha256(url.encode("utf-8")).hexdigest()[:8]
    ext = guess_ext_from_url(url) or fallback_ext
    return f"{base_no_ext}_{h}{ext}"


def download_file(url: str, out_path: Path, timeout: int, logger: logging.Logger) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    headers = {"User-Agent": "md-image-localizer/1.1 (+local)"}

    try:
        with requests.get(url, stream=True, timeout=timeout, headers=headers) as r:
            r.raise_for_status()
            with open(out_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024 * 64):
                    if chunk:
                        f.write(chunk)
    except Exception:
        raise


def iter_image_urls(md: str) -> Iterable[Tuple[str, Tuple[int, int]]]:
    """
    返回 (url, (start, end))，用于替换 md 中对应的 url 子串。
    支持：
    - Markdown: ![alt](url) 或 ![alt](url "title")
    - HTML: <img src="url">
    """
    md_img_re = re.compile(
        r"!\[[^\]]*\]\(\s*(?P<url><[^>]+>|[^)\s]+)\s*(?:\"[^\"]*\"|'[^']*')?\s*\)",
        flags=re.IGNORECASE,
    )
    html_img_re = re.compile(
        r"<img\b[^>]*?\bsrc\s*=\s*(?P<q>['\"])(?P<url>.*?)(?P=q)[^>]*?>",
        flags=re.IGNORECASE | re.DOTALL,
    )

    for m in md_img_re.finditer(md):
        raw = m.group("url").strip()
        if raw.startswith("<") and raw.endswith(">"):
            raw = raw[1:-1].strip()
        yield raw, m.span("url")

    for m in html_img_re.finditer(md):
        raw = m.group("url").strip()
        yield raw, m.span("url")


def localize_images_in_markdown_text(
        md_text: str,
        md_path: Path,
        config: MdImageLocalizeConfig,
        logger: logging.Logger,
) -> Tuple[str, Dict[str, str], Dict[str, str]]:
    """
    返回 (new_md_text, replaced_map, failed_map)
    """
    images_dir = md_path.parent / config.images_dir_name
    replaced: Dict[str, str] = {}
    failed: Dict[str, str] = {}

    occurrences: list[Tuple[str, Tuple[int, int]]] = list(iter_image_urls(md_text))

    # 先收集候选（只处理 http(s) 且 URL path 有明确图片扩展名）
    candidates: Dict[str, str] = {}  # 原始url -> 规范化url
    for raw_url, _ in occurrences:
        if not is_http_url(raw_url):
            continue

        normalized = normalize_url(raw_url, config.fix_alt_media_backslash)
        ext = guess_ext_from_url(normalized)
        if ext is None:
            # 不确定是不是图片（比如无后缀），这里先不动，避免误伤
            continue

        candidates[raw_url] = normalized

    # 下载
    for raw_url, normalized_url in candidates.items():
        ext = guess_ext_from_url(normalized_url) or ".png"
        filename = stable_name_from_url(normalized_url, fallback_ext=ext)
        local_path = images_dir / filename
        rel_path = f"{config.images_dir_name}/{filename}"

        # 已存在则复用
        if local_path.exists() and local_path.stat().st_size > 0:
            replaced[raw_url] = rel_path
            continue

        if config.dry_run:
            replaced[raw_url] = rel_path
            continue

        try:
            download_file(normalized_url, local_path, config.timeout_seconds, logger)
            replaced[raw_url] = rel_path
            logger.info(f"Downloaded: {normalized_url} -> {local_path}")
        except Exception as e:
            failed_reason = f"{type(e).__name__}: {e}"
            failed[raw_url] = failed_reason
            logger.error(
                "Download failed | url=%s | normalized_url=%s | out_path=%s | reason=%s",
                raw_url,
                normalized_url,
                str(local_path),
                failed_reason,
            )

    # 替换文本
    if not replaced:
        return md_text, replaced, failed

    new_md = md_text
    spans_to_replace = []
    for url, span in occurrences:
        if url in replaced:
            spans_to_replace.append((span[0], span[1], replaced[url]))

    spans_to_replace.sort(key=lambda x: x[0], reverse=True)
    for start, end, new_url in spans_to_replace:
        new_md = new_md[:start] + new_url + new_md[end:]

    return new_md, replaced, failed


def process_markdown_file(
        md_file: str,
        config: Optional[MdImageLocalizeConfig] = None,
        logger: Optional[logging.Logger] = None,
) -> MdImageLocalizeResult:
    if config is None:
        config = MdImageLocalizeConfig()
    if logger is None:
        logger = setup_logger()

    md_path = Path(md_file).expanduser().resolve()
    if not md_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {md_path}")

    md_text = md_path.read_text(encoding="utf-8")
    new_md, replaced_map, failed_map = localize_images_in_markdown_text(
        md_text=md_text,
        md_path=md_path,
        config=config,
        logger=logger,
    )

    # 输出路径策略
    if config.output_md_path:
        out_path = Path(config.output_md_path).expanduser().resolve()
    elif config.in_place:
        out_path = md_path
    else:
        out_path = md_path.with_suffix(md_path.suffix + ".localized.md")

    if config.dry_run:
        logger.info("Dry-run enabled: no file will be written.")
    else:
        out_path.write_text(new_md, encoding="utf-8")
        logger.info(f"Written markdown: {out_path}")

    if failed_map:
        logger.warning(f"Some images failed to download: {len(failed_map)} (kept original URLs)")

    return MdImageLocalizeResult(
        input_md=str(md_path),
        output_md=str(out_path),
        images_dir=str((md_path.parent / config.images_dir_name).resolve()),
        replaced_map=replaced_map,
        failed_map=failed_map,
    )

if __name__ == "__main__":
    demo_md = "./doc-localizer/atlantis/atlantis-for-ios.md"
    cfg = MdImageLocalizeConfig(
        images_dir_name="images",
        in_place=False,
        fix_alt_media_backslash=True,
        timeout_seconds=30,
        dry_run=False,
    )

    log = setup_logger(level=logging.INFO)
    try:
        result = process_markdown_file(demo_md, cfg, log)
        log.info(f"Replaced: {len(result.replaced_map)}, Failed: {len(result.failed_map)}")
    except Exception as ex:
        log.error(f"Process failed: {type(ex).__name__}: {ex}")
