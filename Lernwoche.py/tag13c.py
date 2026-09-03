# Tag 13: Produkte nur bei ausreichendem Bestand entnehmen

lager = {
    "Apfel": 3,
    "Milch": 1,
    "Brot": 2
}

produkt = input("Welches Produkt wurde entnommen? ")

if produkt in lager:
    try:
        menge = int(input("Wie viele wurden entnommen? "))

        if 0 < menge <= lager[produkt]:
            lager[produkt] -= menge 
            print(f"Restbestand: {lager[produkt]}")
        else:
            print("Ungültige Menge oder Bestand zu klein. ")
    except ValueError:
        print("Bitte eine ganze Zahl eingeben. ")

else:
    print("Produkt nicht im Lager. ")

