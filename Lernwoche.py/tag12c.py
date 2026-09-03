# Tag 12: Vor dem Zugriff prüfen, ob ein Schlüssel existiert

einkauf = {
    "Apfel": 3,
    "Milch": 1, 
    "Brot": 2,
    "Mandeln": 4,

}

gesucht = input("Welches Produkt suchst du? ")

if gesucht in einkauf:
    print(f"{gesucht}: {einkauf[gesucht]}")
else:
    print ("Produkt nicht gefunden.")

