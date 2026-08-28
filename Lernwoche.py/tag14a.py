import json

lager = {
    "Apfel": 3,
    "Milch": 1,
    "Brot": 2
}


with open("Lernwoche.py/lager.json", "w", encoding="utf-8") as datei:
    json.dump(lager, datei, ensure_ascii=False, indent=4)

print("Lager gespeichert.")
