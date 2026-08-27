lager = {
    "Apfel": 3,
    "Milch": 1,
    "Brot": 2
}

produkte = input("Welches Produkt wure geliefert? ")

if produkte in lager:
    try:
        menge = int(input("Wie viele wurden geliefert? "))
        lager[produkte] += menge
        print(f"Neuer Bestand: {lager[produkte]}")
    except ValueError:
        print("Bitte eine ganze Zahl eingeben. ")
else:
    print("Produkte nicht im Lager.")

         