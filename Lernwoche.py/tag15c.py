# Tag 15: Fehlerbehandlung beim Laden in eine Funktion kapseln

import json

# Lagerbestand laden und mögliche Dateifehler abfangen
def lager_laden():
    try:
        with open("Lernwoche.py/lager.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return{}
    except json.JSONDecodeError:
        return {}

# Hauptprogramm: Lager laden und anzeigen
lager = lager_laden()
print(lager)
