from spider import *
import re
from bs4 import BeautifulSoup


Base_URL = f'https://studio.code.org/s/csp1-2023'



def request_webpage(unit, lesson):
    unit = 1
    lesson = 1
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



if __name__ == '__main__':
    a = request_webpage(1, 1)
    print(a)
    b = process_html(a)
    c = process_link(b)
    print(c)
