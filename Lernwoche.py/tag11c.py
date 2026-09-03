# Tag 11: Ein Produkt an eine bestehende Datei anhängen

produkt = input("Welches Produkt möchtest du hinzufügen: ")

with open("einkaufsliste.txt", "a", encoding="utf-8") as datei:
    datei.write(produkt + "\n" )

print("Produkt hinzugefügt!")
