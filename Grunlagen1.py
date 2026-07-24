# Eine leere einkaufsliste erstellen 
einkaufsliste = []
def liste_anzeigen ():
    print("\n--- DEINE EINKAUFSLISTE ---")
    if not einkaufsliste:
        print("Deine Einkaufsliste ist leer!")
    else:
        for index, item in enumerate(einkaufsliste, start=1):
            print(f"{index}. {item}")
            print("---------------------------")
# Hauptprogramm mit Schleife
while True:
                liste_anzeigen()
                print ("Aktionen: (1) Artikel hinzufügen, (2) Artikel entfernen, (3) Beenden")
                wahl = input("Was möchtest du tun? (1/2/3): ")
                if wahl == "1":
                    element = input ("Was möchtest du hinzufügen? ")
                    einkaufsliste.append(element) # .append() fuegt etwas zur Liste hinzu 
                    print(f"{element} wurde zur Einkaufsliste hinzugefügt.")
                elif wahl == "2":
                    if einkaufsliste: 
                        nummer = int(input("Welche Nummer möchtest du entfernen? "))
                        if 1 <= nummer <= len(einkaufsliste):
                            entferntes_element = einkaufsliste.pop(nummer - 1) # .pop() entfernt ein Element aus der Liste
                            print(f"{entferntes_element} wurde von der Einkaufsliste entfernt.")
                        else:
                            print("Ungültige Nummer. Bitte wähle eine gültige Nummer.")
                    else:
                        print("Die Einkaufsliste ist leer. Es gibt nichts zu entfernen.")
                elif wahl == "3":
                    print ("Tschüss! Viel Spass beim Einkaufen!")
                else: 
                    print("Ungültige Wahl. Bitte wähle 1, 2 oder 3.")