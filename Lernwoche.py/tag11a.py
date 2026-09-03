# Tag 11: Eine Einkaufsliste erfassen und in eine Datei schreiben

liste = []


for i in range(3):

    produkt = input("Gib ein Proukt ein: ")
    liste.append(produkt)

with open("einkaufsliste.txt", "w", encoding="utf-8") as datei:
    for produkt in liste:
        datei.write(produkt + "\n")

print("Einkaufsliste gespeichert!")
