import requests
from requests import RequestException
import os
from urllib.parse import urlparse, unquote
import xml.etree.ElementTree as ET


def run_crawler(links: list):
    for link in links:
        try:
            url = link + ".md"
            file_path = create_file_from_url(url)
            print(f"url:{url}, file_path: {file_path}")
            if not os.path.exists(file_path):
                content = request_content(url)
                write_file_content(file_path, content)
        except RequestException as e:
            print(e)


def get_headers() -> dict:
    return {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'
    }


def request_content(url):
    try:
        headers = get_headers()
        response = requests.get(url, timeout=5, headers=headers)
        # 如果状态码不是 2xx，抛出异常
        response.raise_for_status()
        print("请求成功：", response.text)
        return response.text
    except RequestException as e:
        print("请求失败：", str(e))


def write_file_content(filename: str, content: str):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


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

    # 创建目录
    os.makedirs(os.path.dirname(local_path), exist_ok=True)

    # 返回文件路径
    return local_path


def query_sitemap() -> str:
    """
    请求 sitemap, 返回 sitemap 内容
    :return:
    """
    sitemap_url = 'https://docs.proxyman.com/sitemap-pages.xml'
    headers = get_headers()
    response = requests.get(sitemap_url, headers=headers)
    return response.text


def parse_sitemap_content_extra_urls(file_content: str):
    root = ET.fromstring(file_content)
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = [loc.text for loc in root.findall('.//ns:loc', namespace)]
    for i, url in enumerate(urls, 1):
        print(f"{i}. {url}")
    urls.append(f'https://docs.proxyman.com/readme')
    return urls


def run():
    file_content = query_sitemap()
    set_urls = set(parse_sitemap_content_extra_urls(file_content))
    run_crawler(list(set_urls))
    print(file_content)


if __name__ == "__main__":
    run()
