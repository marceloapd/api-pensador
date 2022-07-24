import re
import math
import requests
from bs4 import BeautifulSoup

def get_phrases(term, max):
    page = requests.get(f'https://www.pensador.com/{term}')
    soup = BeautifulSoup(page.text, 'html.parser')
    description = soup.find("div", class_="description").text
    quantity_phrases = int(re.search("\s(\d+)\sfrases", description).group(1))
    if max == 0:
        quantity_pages = math.ceil(quantity_phrases/20)
    else:
        quantity_pages = max

    phrases_object = {"total": quantity_phrases, "searchTerm": term, "phrases": []}

    for i in range(1,quantity_pages+1):
        phrases_lists = soup.findAll("p")
        phrases_author = soup.findAll("div", class_="autor")
        for (phrase,author) in zip(phrases_lists,phrases_author):
            author = author.text.replace("\n", "")
            phrases_object['phrases'].append({"author": author,"text": phrase.text})
        page = requests.get(f'https://www.pensador.com/plantas/{i}')
        soup = BeautifulSoup(page.text, 'html.parser')

    return phrases_object