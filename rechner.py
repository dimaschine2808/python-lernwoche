def addiere(a, b):
    return a + b

def subtrahiere(a, b):
    return a - b

print("Willkommen zum Mini-Rechner!")
zahl1 = float(input("Erste Zahl: "))
zahl2 = float(input("Zweite Zahl: "))

print(f"Summe: {addiere(zahl1, zahl2)}")
print(f"Differenz: {subtrahiere(zahl1, zahl2)}")