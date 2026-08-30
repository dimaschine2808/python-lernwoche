import json

def lager_speichern(lager):
    with open("Lernwoche.py/lager_test.json", "w", encoding="utf-8") as file:
        json.dump(lager, file, ensure_ascii=False, indent=4)

lager = {
    "Apfel": 5,
    "Milch": 2
}

lager_speichern(lager)
print("Lager gespeichert")
