from bs4 import BeautifulSoup
import requests
import pandas as pd

file = pd.read_csv("E:/Prywatne/PENDRIVE BACKUP/programowanie/Python/plik.txt", header=None, names=["link"])
file_unique = file.drop_duplicates(subset=["link"], keep='first').reset_index(drop=True)

for url in file_unique["link"]:
    print("----------------")
    print(f"Pobieram stronę: {url}")
    print("----------------")
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Błąd pobierania strony: {url}")
        continue
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    prices = soup.find_all("p", attrs={"class":"ml-1 inline pt-1 max-768:text-base 1024:text-2xl 768:text-2xl text-xl font-medium text-overcez-primary"})
    names = soup.find_all("h1", attrs={"class":"1024:text-2xl 768:text-2xl text-xl font-medium text-overcez-primary"})
    descriptions = soup.find_all("div", attrs={"class":"mr-4 mt-4 text-xs font-light text-overcez-primary/50 1280:text-sm/5"})
    sizes = soup.find_all("input", attrs={"class":"css-1hac4vs-dummyInput"})
    
    for price in prices:
        print(f"Cena: {price.text.strip()}")
    for name in names:
        print(f"Nazwa: {name.text.strip()}")
    for description in descriptions:
        print(f"Opis: {description.text.strip()}")
    for size in sizes:
        print(f"rozmiar: {size.text.strip()}")
