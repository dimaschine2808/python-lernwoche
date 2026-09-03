# Tag 13: Mengen sicher einlesen und zum Lagerbestand addieren

lager =  {
    "Apfel": 3,
    "Milch": 1,
    "Brot": 2,
}
produkt = input("Welches Produkt wurde geliefert? ")

try:
    menge = int(input("Wie viele wurden geliefert? "))
    lager[produkt] = lager.get(produkt, 0) + menge 
    print(f"Neuer Bestand: {lager[produkt]}")
except ValueError:
    print("Bitte eine ganze Zahl eingeben. ")


