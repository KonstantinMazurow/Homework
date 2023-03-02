import requests
from bs4 import BeautifulSoup as bs


def get_joke(url):
    r = requests.get(url)
    print(r.status_code)
    soup = bs(r.text, "html.parser")
    joke = str(soup.find('table', class_='text').text)
    return joke