from typing import List
import os
from urllib.parse import urlparse, unquote
import re
import urllib.parse
from markdown_localizer import process_markdown_file, MdImageLocalizeConfig, MdImageLocalizeResult
from pathlib import Path


def list_files_scandir(directory: str, recursive: bool = True) -> List[str]:
    """
    使用 os.scandir 遍历文件
    Args:
        directory: 要遍历的目录
        recursive: 是否递归遍历子目录
    Returns:
        文件路径列表
    """
    files = []

    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    files.append(entry.path)
                elif entry.is_dir() and recursive:
                    # 递归处理子目录
                    subdir_files = list_files_scandir(entry.path, recursive)
                    files.extend(subdir_files)
    except PermissionError:
        print(f"无权限访问目录: {directory}")
    except FileNotFoundError:
        print(f"目录不存在: {directory}")

    return files


def read_content(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()


def save(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)


def create_file_from_url(url, base_dir='doc-localizer'):
    """
    解析URL并创建对应的本地文件

    Args:
        url: 完整的URL地址
        base_dir: 本地存储的基础目录
    """
    # 解析URL
    parsed = urlparse(url)

    # 解码URL编码的路径
    path = unquote(parsed.path)

    # 移除路径开头的斜杠
    if path.startswith('/'):
        path = path[1:]

    # 构建完整的本地文件路径
    local_path = os.path.join(base_dir, path)

    # 创建目录（如果不存在）
    os.makedirs(os.path.dirname(local_path), exist_ok=True)

    # 返回文件路径
    return local_path


# 高级版本：更精确地解析 Markdown
def advanced_extract_png_urls(content: str):
    """更高级的 Markdown 解析，处理更多格式"""

    png_urls = []

    # 1. 处理标准的 Markdown 图片语法 ![](url)
    md_img_pattern = r'!\[[^\]]*\]\(([^)]+)\)'
    for match in re.finditer(md_img_pattern, content):
        url = match.group(1)
        if url and check_is_png(url):
            png_urls.append(url)

    # 2. 处理 HTML <img> 标签
    html_img_pattern = r'<img[^>]+src="([^"]+)"[^>]*>'
    for match in re.finditer(html_img_pattern, content):
        url = match.group(1)
        if url and check_is_png(url):
            png_urls.append(url)

    # 3. 处理纯文本中的 URL
    url_pattern = r'\bhttps?://[^\s<>"\'{}|\\^`\[\]()]+\b'
    for match in re.finditer(url_pattern, content):
        url = match.group(0)
        if url and check_is_png(url):
            png_urls.append(url)

    return png_urls


def check_is_png(url: str):
    """处理单个 URL：解码并检查是否为 PNG"""
    decoded_url = urllib.parse.unquote(url)

    # 更精确的 PNG 检测
    # 检查 URL 路径以 .png 结尾，或者查询参数前包含 .png
    parsed = urllib.parse.urlparse(decoded_url)
    path = parsed.path.lower()

    # 检查是否是 PNG
    is_png = (
            path.endswith('.png') or
            '.png?' in path or
            '.png#' in path or
            '.png' in path
    )

    return is_png


def replace_localizer(md_file: str) -> MdImageLocalizeResult:
    """
        images_dir_name: str = "images"  # 图片保存目录（相对 md 文件同级目录）
        timeout_seconds: int = 30
        dry_run: bool = False
        in_place: bool = False
        output_md_path: Optional[str] = None  # 优先级最高（如果设置，则忽略 in_place）
        fix_alt_media_backslash: bool = False  # 开关：alt=media\\ -> alt=media
    """
    cfg = MdImageLocalizeConfig(
        images_dir_name="images",
        in_place=True,
        fix_alt_media_backslash=True,
        timeout_seconds=60,
    )
    result = process_markdown_file(md_file, cfg)
    print(result.replaced_map)  # 成功替换的
    print(result.failed_map)  # 下载失败的（会保留原 URL 不改）
    return result


def get_suffix(path_str: str) -> str:
    return Path(path_str).suffix  # 包含点，比如 ".md"


def run():
    MD_EXTS = {".md", ".markdown", ".mdx"}
    # 使用示例
    file_paths = list_files_scandir("./doc-localizer")
    print(f"file size: {len(file_paths)}")
    for file_path in file_paths:
        suffix = get_suffix(file_path)
        if suffix.lower() in MD_EXTS:
            result = replace_localizer(file_path)
            print(file_path)
            print(result)


if __name__ == "__main__":
    run()
