import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def download_pics(url, save_as):
    response = requests.get(url)

    if response.status_code == 200:
        with open(save_as, 'wb') as f:
            f.write(response.content)

def download_pics_from_file(dm01Img):
    with open(dm01Img, 'r') as fi:
        urls = fi.readlines()

    for url in urls:
        parsed_url = urlparse(url)
        save_as = parsed_url.path.split('/')[-1]

        download_pics(url, save_as)