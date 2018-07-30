import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp
import sys
import re

def find_between(s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""


miasto = "katowice"
fraza = "do remontu"
deal = "sprzedaz"
nrstrony = 1
page = requests.get('https://www.otodom.pl/'+deal+'/mieszkanie/'+miasto+'/q-'+fraza+'/?page='+str(nrstrony) )

soup = BeautifulSoup(page.text, 'html.parser')

ilosc_ofert = soup.find(class_="offers-index pull-left text-nowrap").contents[1]
ilosc_ofert = int(find_between(str(ilosc_ofert), "<strong>", "</strong>"))
print("Znalezione oferty: " + str(ilosc_ofert))

items_maincontent = soup.find(class_="col-md-content")
items = items_maincontent.find_all(class_="offer-item")
print("Ilość głównych itemów: " + str(len(items)) + "\n")

# for item in items:

# print(item.prettify())
item = items[0]
print(item.prettify())
title = item.find(class_="offer-item-title")
address_str = item.find(class_="text-nowrap hidden-xs")
rooms_str = item.find(class_="offer-item-rooms hidden-xs")
price_str = item.find(class_="offer-item-price")
area_str = item.find(class_="hidden-xs offer-item-area")
price_per_meter_str = item.find(class_="hidden-xs offer-item-price-per-m")
footer_str = item.find(class_="params-small clearfix hidden-xs")
tracking_id = item.attrs["data-tracking-id"]

print("Tytuł: " + str(title.contents[0]))
address = address_str.contents[0].replace("Mieszkanie na sprzedaż: ", "")
print("Adres: " + str(address))
rooms = int(rooms_str.contents[0].replace(" ", "").replace("pokoje", ""))
print("Pokoje: " + str(rooms))
price = int(price_str.contents[0].replace(" ", "").replace("\n", "").replace("zł", ""))
print("Cena: " + str(price))
area = float(area_str.contents[0].replace(" m²", "").replace(",", "."))
print("Powierzchnia: " + str(area))
price_per_meter = float(price_per_meter_str.contents[0].replace(" zł/m²", "").replace(" ", ""))
print("Cena za metr: " + str(price_per_meter))
footer = footer_str.contents[1]
if footer.find("Oferta prywatna") == -1:
    print("Oferta prywatna: NIE")
else:
    print("Oferta prywatna: TAK")
print("Tracking_id: " + str(tracking_id))


sys.exit()
# Remove bottom links
# soup.find(class_='AlphaNav').decompose()
# r
