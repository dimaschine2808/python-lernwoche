# Tag 16: Laden, Speichern und Hinzufügen in Funktionen aufteilen

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


# Produkt neu anlegen oder vorhandenen Bestand erhöhen
def produkt_hinzufuegen(lager, produkt, menge):
    lager[produkt] = lager.get(produkt, 0) + menge 




# Hauptprogramm: Produkte hinzufügen und Ergebnis speichern
lager = lager_laden()
produkt_hinzufuegen(lager, "Birnen", 4)
produkt_hinzufuegen(lager, "Birnen", 3)
print(lager)

lager_speichern(lager)
print("Lager gespeichert")

