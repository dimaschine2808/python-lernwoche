# Tag 16: Laden und Speichern in getrennte Funktionen aufteilen

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


# Lagerbestand in einer JSON-Datei speichern
def lager_speichern(lager):
    with open("Lernwoche.py/lager_test.json", "w", encoding="utf-8") as file:
        json.dump(lager, file, ensure_ascii=False, indent=4)


# Hauptprogramm: Lager laden, anzeigen und speichern
lager = lager_laden()
print(lager)

lager_speichern(lager)
print("Lager gespeichert")



