import json 

with open("Lernwoche.py/lager.json", "r", encoding="utf-8") as datei:
    lager = json.load(datei)

produkt = input("Welches Produkt wurde geliefert? ")
menge = int(input("Wie viele wurden geliefert? "))

lager[produkt] = lager.get(produkt, 0) + menge

with open("Lernwoche.py/lager.json", "w", encoding="utf-8") as datei:
    json.dump(lager, datei, ensure_ascii=False, indent=4)
    

print(lager)

