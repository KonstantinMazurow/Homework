import requests
from bs4 import BeautifulSoup as bs


def get_books_list():
    URL_TEMPLATE = "https://www.100bestbooks.ru"
    r = requests.get(URL_TEMPLATE)
    print(r.status_code)
    soup = bs(r.text, "html.parser")
    data = soup.find('table', class_='table-rating').find_all('span')
    books = []
    for row in data:
        books.append(row.get_text())
    x = 0
    y = 3
    books_turtle = []
    for i in range(100):
        b = tuple(books[x:y])
        books_turtle.append(b)
        x += 3
        y += 3
    return(books_turtle)
