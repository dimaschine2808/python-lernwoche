# Tag 14: Einen Lagerbestand aus einer JSON-Datei laden

import json

with open("Lernwoche.py/lager.json", "r", encoding="utf-8") as datei:
    lager = json.load(datei)

for produkt, menge in lager.items():
    print(f"{produkt}: {menge}")
