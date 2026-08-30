import json

def lager_laden():
    try:
        with open("Lernwoche.py/lager.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return{}
    except json.JSONDecodeError:
        return {}

lager = lager_laden()
print(lager)
