# 7. Data scraping

import requests #$ python -m pip install requests
from bs4 import BeautifulSoup #$ python -m pip install beautifulsoup4

def scrapper(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all("span", class_="price-box__price")

    numbers = []

    for element in elements:
        x = ''.join(element.findAll(text=True))
        x = x.replace("€","").replace(" ","").replace(",","")
        x = int(x)
        numbers.append(x)
    #print(numbers)
    return round(sum(numbers) / len(numbers), 2)

print('Average price is ',end='')
print(scrapper("https://www.boataround.com/search?checkIn=2022-06-04&checkOut=2022-06-11&category=sailing-yacht&destinations=zadar-1&reviewScore=7-"),end='')
print(' €',end='')

#Average price is 2115.67 €
