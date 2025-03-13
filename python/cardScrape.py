import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from tqdm import tqdm
from time import sleep  # import time

with open('dm01') as f:
    urls = f.readlines()
    urls = [url.strip() for url in urls]
    f.close()

def remove_empty_lines(text):
    lines = text.split('\n')
    non_empty_lines = filter(lambda line: line.strip() != '', lines)
    return '\n'.join(non_empty_lines)

for i in tqdm(range(0, 100), desc="Fetching DM-01"):
    sleep(0.1)
    for url in urls:
        get_request = requests.Request('GET', url)
        prepped = get_request.prepare()
        response = requests.Session().send(prepped)
        soup = BeautifulSoup(response.text, 'html.parser')
        with open("dm01Info", "a") as f:
            print(remove_empty_lines(soup.get_text()), file=f)

with open('dm02') as f:
    urls = f.readlines()
    urls = [url.strip() for url in urls]
    f.close()

def remove_empty_lines(text):
    lines = text.split('\n')
    non_empty_lines = filter(lambda line: line.strip() != '', lines)
    return '\n'.join(non_empty_lines)

for i in tqdm(range(0, 100), desc="Fetching DM-02"):
    sleep(0.1)
    for url in urls:
        get_request = requests.Request('GET', url)
        prepped = get_request.prepare()
        response = requests.Session().send(prepped)
        soup = BeautifulSoup(response.text, 'html.parser')
        with open("dm02Info", "a") as f:
            print(remove_empty_lines(soup.get_text()), file=f)
