# 1. Funktionen für ie Rechenarten definieren
def addiere(a, b):
    return a + b

def subtrahiere(a, b):
    return a - b

def multipliziere(a, b):
    return a * b

def dividiere(a, b):
    if b == 0:
        return "Fehler: Teilen durch 0 ist nicht erlaubt."
    return a / b
# 2. Hauptprogramm
print ("=== DEIN PERSONAL CALCULATOR == ")
print ("Wähle deine option:")
print ("1. Addition")
print ("2. Subtraktion")
print ("3. Multiplikation")
print ("4. Division")
wahl = input("Gib die Zahl deiner Wahl ein (1/2/3/4): ")
# Zahlen vom Nutzer abfragen (float erlaubt auch Kommazahlen)
zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib die zweite Zahl ein: "))
# 3. Das passende Ergebnis berechnen 
if wahl == "1": 
    ergebnis = addiere( zahl1, zahl2 )
elif wahl == "2":
    ergebnis  = subtrahiere(zahl1, zahl2)
elif wahl == "3":
    ergebnis = multipliziere(zahl1, zahl2)
elif wahl == "4":
    ergebnis = dividiere(zahl1, zahl2)
else:
    ergebnis = "Ungültige Wahl. Bitte wähle eine Zahl zwischen 1 und 4."
print(f"\nErgebnis: {ergebnis}")