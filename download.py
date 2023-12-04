import re
import requests


def download_file_from_google_drive(link, file_path):
    download_url = f'{link}'
    response = requests.get(download_url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully and saved as {file_path}")
    else:
        print("Failed to download the file. Please check the link and try again.")



if __name__ == '__main__':
    download_file_from_google_drive("https://docs.google.com/document/d/1Ycz0b-nlvTSMQPq4dV5MHffdJpZYw-2sPsLAVue4raE/export?format=pdf", r"C:\Users\xieho\PycharmProjects\csp_course_crawler\test.pdf")