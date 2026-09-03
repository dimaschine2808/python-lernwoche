# Tag 18: Auswahlmöglichkeiten mit einem einfachen Menü steuern

print("--- Lagerverwaltung ---")
print("1 - Lager anzeigen")
print("2 - Produkt hinzufügen")
print("0 - Beenden")

auswahl = input("Deine Auswahl: ")

if auswahl == "1":
    print("Lager wird angezeigt")
elif auswahl == "2":
    print("Produkt wird hinzugefuegt ")
elif auswahl == "0":
    print("Programm beendet")
else:
    print("Ungueltige Auswahl")
