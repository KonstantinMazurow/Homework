from data.config import LINK
import requests


def get_pictures():
    r = requests.get(LINK)
    data = r.json()
    return data['message']
