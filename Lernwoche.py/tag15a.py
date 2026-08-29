import json

try:
    with open("Lernwoche.py/lager.json", "r", encoding="utf-8") as file:
        lager = json.load(file)
except FileNotFoundError:
    lager = {}
    print("Noch keine Lagerdatei vorhanden.")

print(lager)
