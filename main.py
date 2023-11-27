from spider import *
import re
from bs4 import BeautifulSoup


def get_source_url():
    unit = 1
    lesson = 1
    while True:
        html = request_webpage(unit, lesson)
        lesson += 1
        if not html:
            lesson = 1
            unit += 1
            continue
        links = process_html(html)
        processed_links = process_link(links)
        print(processed_links)


def request_webpage(unit, lesson):
    url = f"https://studio.code.org/s/csp{unit}-2023/lessons/{lesson}"
    return askUrl(url)


def process_html(html_content):
    try:
        pattern = r'https://[^\s"\'<>]+'
        links = re.findall(pattern, html_content)
        return links
    except Exception as e:
        print(f"ERROR: {e}")
        return []


def process_link(links):
    filtered_links = [link for link in links if
                      "docs.google.com" in link or "youtu.be" in link or "youtube.com" in link]
    return filtered_links


"""def download_link(link):"""
