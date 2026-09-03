# Tag 15: Fehlende und fehlerhafte JSON-Dateien getrennt behandeln

import json

try:
    with open("Lernwoche.py/lager.json", "r", encoding="utf-8") as file:
        lager = json.load(file)
except FileNotFoundError:
    lager = {}
    print("Noch keine Lagerdatei vorhanden.")
except json.JSONDecodeError:
    lager = {}
    print("Die Lagerdatei enthaehlt ungueltige Daten.")

print(lager)
