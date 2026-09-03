# Tag 15: Einen JSON-Ladefehler beobachten und die Datei neu schreiben

import json



with open ("Lernwoche.py/lager.json", "r", encoding="utf-8") as datei:
    lager = json.load(datei)

lager["Milch"] += 2 

with open ("Lernwoche.py/lager.json", "w", encoding="utf-8") as datei:
    json.dump(lager,datei, ensure_ascii=False, indent=4)


