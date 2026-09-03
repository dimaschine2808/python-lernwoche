# Tag 6: Wörter in einem Dictionary suchen und alle Paare ausgeben

vokabeln = {"Blume":  "Flower", "Auto": "Car", "Tisch": "Desk", "Turm": "Tower", "Katze": "Cat"}

wort= input("Was ist das Wort? ")

if wort in vokabeln: 
   print (vokabeln[wort]) 
else: 
    print(" Wort nicht gefunden!")





for deutsch, englisch  in vokabeln.items():
    print ( deutsch , englisch)
