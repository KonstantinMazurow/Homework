import requests
# Inflect is useful for natural language generation and has a method for turning numbers into english text.
import inflect

def response():
    r = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a')
    data = r.json()
    a = ''
    count = 1
    p = inflect.engine()
    for item in data['drinks']:
        c = p.number_to_words(count)
        a += (f"Element {c}:\n \tName: {item['strDrink']}\n \tDescription: {item['strInstructions']}\n \tPicture: {item['strDrinkThumb']} \n")
        count += 1
    return a
        
def record(x):
    # Path to the file being written. I have it in the folder "Homework 6"
    with open('Homework 6/cocktails.txt', 'w+') as f: 
        f.write(x)       

record(response())
