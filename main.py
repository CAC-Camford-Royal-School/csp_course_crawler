from spider import *
from utils import *


def get_source_url():
    unit = 1
    lesson = 1
    while unit < 12:
        html = request_webpage(unit, lesson)
        if not html:
            lesson = 1
            unit += 1
            continue
        links = process_html(html)
        processed_links = process_link(links)
        directory = f'files/unit{unit}/lesson{lesson}/'
        download_file(processed_links, directory)
        lesson += 1


def request_webpage(unit, lesson):
    url = f"https://studio.code.org/s/csp{unit}-2023/lessons/{lesson}"
    return ask_url(url)


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
    processed_links = [link_download(link) for link in filtered_links]
    return processed_links


def link_download(link):
    pattern = r"https://docs\.google\.com/([a-zA-Z0-9/_-]+?)/edit"

    if "docs.google.com" in link:
        match = re.search(pattern, link)
        # Check if the match object is not None and has a group to extract
        if match and match.groups():
            extracted_content = match.group(1)
            return f"https://docs.google.com/{extracted_content}/export?format=pdf"
        else:
            # If no match is found, return nothing
            return None
    else:
        return link


if __name__ == '__main__':
    get_source_url()
