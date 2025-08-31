from bs4 import BeautifulSoup
import requests

page_to_scrap = requests.get("https://overcez.pl/produkt/Air-Jordan-5-Retro-Awake-NY-Black-p776060580/")
soup = BeautifulSoup(page_to_scrap.text, "html.parser")
prices = soup.find_all("p", attrs={"class":"ml-1 inline pt-1 max-768:text-base 1024:text-2xl 768:text-2xl text-xl font-medium text-overcez-primary"})
names = soup.find_all("h1", attrs={"class":"1024:text-2xl 768:text-2xl text-xl font-medium text-overcez-primary"})
descriptions = soup.find_all("div", attrs={"class":"mr-4 mt-4 text-xs font-light text-overcez-primary/50 1280:text-sm/5"})

for price in prices:
    print(f"Cena: {price.text}")
for name in names:
    print(f"Nazwa: {name.text}")
for description in descriptions:
    print(f"Opis: {description.text}")
