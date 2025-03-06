import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup

with open('dm01') as f:
    urls = f.readlines()
    urls = [url.strip() for url in urls]
    f.close()

def remove_empty_lines(text):
    lines = text.split('\n')
    non_empty_lines = filter(lambda line: line.strip() != '', lines)
    return '\n'.join(non_empty_lines)

for url in urls:
    get_request = requests.Request('GET', url)
    prepped = get_request.prepare()
    response = requests.Session().send(prepped)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open("dm01Info", "a") as f:
        print(remove_empty_lines(soup.get_text()), file=f)