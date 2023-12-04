import requests
import re
import os


def download_file(urls, save_path):
    for url in urls:
        if url:
            if 'google' in url:
                response = requests.get(url)
                path = save_path + get_filename(url) + '.pdf'
                save_file(response.content, path)
            else:
                path = save_path + url[-5:] + '.txt'
                save_file(bytes(url, encoding='utf-8'), path)


def save_file(content, save_path):
    folder_path = os.path.dirname(save_path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    with open(save_path, 'wb') as file:
        file.write(content)


def get_filename(url):
    response = requests.head(url)
    content_disposition = response.headers.get("content-disposition")

    if content_disposition:
        # 通过正则表达式从 Content-Disposition 中提取文件名
        match = re.search(r'filename="(.+)"', content_disposition)
        if match:
            return match.group(1)

    # 如果 Content-Disposition 中没有文件名，使用 URL 中的路径部分
    return url.split('/')[5][-5:]


if __name__ == "__main__":
    pass
