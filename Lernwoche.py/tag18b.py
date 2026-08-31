import json
from pathlib import Path


DATEIPFAD = Path(__file__).with_name("lager.json")


def lager_laden():
    try:
        with open(DATEIPFAD, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def lager_speichern(lager):
    with open(DATEIPFAD, "w", encoding="utf-8") as file:
        json.dump(lager, file, ensure_ascii=False, indent=4)


def produkt_hinzufuegen(lager, produkt, menge):
    lager[produkt] = lager.get(produkt, 0) + menge


def menge_einlesen():
    while True:
        try:
            return int(input("Welche Menge möchtest du hinzufügen? "))
        except ValueError:
            print("Bitte gib eine ganze Zahl ein.")


lager = lager_laden()

while True:
    print("--- Lagerverwaltung ---")
    print("1 - Lager anzeigen")
    print("2 - Produkt hinzufügen")
    print("0 - Beenden")

    auswahl = input("Deine Auswahl: ")


    if auswahl == "1":
        print(lager)
    elif auswahl == "2":
        produkt = input("Welches Produkt moechtest du hinzufuegen? ").strip()

        while not produkt:
            print("Bitte gib einen Produktnamen ein. ")
            produkt = input("Welches Produkt moechtest du hinzufuegen? ").strip()
        menge = menge_einlesen()
        produkt_hinzufuegen(lager, produkt, menge)
        lager_speichern(lager)
        print(f"{produkt} wurde mit der Menge {menge} hinzugefuegt. ")
    elif auswahl == "0":
        print("Programm beendet")
        break
    else:
        print("Ungueltige Auswahl")




