import json


def lager_laden():
    try:
        with open("Lernwoche.py/lager.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return{}
    except json.JSONDecodeError:
        return {}


def lager_speichern(lager):
    with open("Lernwoche.py/lager_test.json", "w", encoding="utf-8") as file:
        json.dump(lager, file, ensure_ascii=False, indent=4)


def produkt_hinzufuegen(lager, produkt, menge):
    lager[produkt] = lager.get(produkt, 0) + menge 




lager = lager_laden()
produkt_hinzufuegen(lager, "Birnen", 4)
produkt_hinzufuegen(lager, "Birnen", 3)
print(lager)

lager_speichern(lager)
print("Lager gespeichert")

