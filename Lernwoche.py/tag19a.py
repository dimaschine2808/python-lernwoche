# Tag 19: Produkte sicher entnehmen und negativen Bestand verhindern

import json
from pathlib import Path


DATEIPFAD = Path(__file__).with_name("lager.json")


# Lagerbestand laden und mögliche Dateifehler abfangen
def lager_laden():
    try:
        with open(DATEIPFAD, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


# Lagerbestand in der JSON-Datei speichern
def lager_speichern(lager):
    with open(DATEIPFAD, "w", encoding="utf-8") as file:
        json.dump(lager, file, ensure_ascii=False, indent=4)


# Produkt neu anlegen oder vorhandenen Bestand erhöhen
def produkt_hinzufuegen(lager, produkt, menge):
    lager[produkt] = lager.get(produkt, 0) + menge


# Produkt nur bei gültiger Menge und ausreichendem Bestand entnehmen
def produkt_entnehmen(lager, produkt, menge):
    if produkt not in lager:
        print("Produkt nicht im Lager.")
        return False

    if menge <= 0:
        print("Die Menge muss größer als 0 sein.")
        return False

    if menge > lager[produkt]:
        print("Bestand zu klein.")
        return False

    lager[produkt] -= menge
    print(f"Restbestand: {lager[produkt]}")
    return True


# Menge so lange abfragen, bis eine positive ganze Zahl eingegeben wurde
def menge_einlesen(aktion):
    while True:
        try:
            menge = int(input(f"Welche Menge möchtest du {aktion}? "))
            if menge > 0:
                return menge
            print("Bitte gib eine positive ganze Zahl ein.")
        except ValueError:
            print("Bitte gib eine ganze Zahl ein.")


# Hauptprogramm: Lager laden und Menü wiederholt anzeigen
lager = lager_laden()

while True:
    print("--- Lagerverwaltung ---")
    print("1 - Lager anzeigen")
    print("2 - Produkt hinzufügen")
    print("3 - Produkt entnehmen")
    print("0 - Beenden")

    auswahl = input("Deine Auswahl: ")


    if auswahl == "1":
        print(lager)
    elif auswahl == "2":
        produkt = input("Welches Produkt moechtest du hinzufuegen? ").strip()

        while not produkt:
            print("Bitte gib einen Produktnamen ein. ")
            produkt = input("Welches Produkt moechtest du hinzufuegen? ").strip()
        menge = menge_einlesen("hinzufügen")
        produkt_hinzufuegen(lager, produkt, menge)
        lager_speichern(lager)
        print(f"{produkt} wurde mit der Menge {menge} hinzugefuegt. ")
    elif auswahl == "3":
        produkt = input("Welches Produkt möchtest du entnehmen? ").strip()

        while not produkt:
            print("Bitte gib einen Produktnamen ein.")
            produkt = input("Welches Produkt möchtest du entnehmen? ").strip()

        menge = menge_einlesen("entnehmen")
        if produkt_entnehmen(lager, produkt, menge):
            lager_speichern(lager)
    elif auswahl == "0":
        print("Programm beendet")
        break
    else:
        print("Ungueltige Auswahl")




