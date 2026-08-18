#Tag 1  #Values

name = "Mia Herget"
alter = 20 
print (name)
print (alter)
jahr_100 = 2026 + (100 - alter)
print (f"Du wirst im {jahr_100} 100 Jahre alt sein")

#Tag 2  #float und input

zahl_1 = float(input("Gib deine erste Zahl ein:")) 
zahl_2 = float(input("Gib deine zweite Zahl ein:"))

print (f"Summe: {zahl_1 + zahl_2}")
print (f"Subtraktion: {zahl_1 - zahl_2}")
print (f"Multiplikation: {zahl_1 * zahl_2}")
print (f"Division: {zahl_1 / zahl_2}")

#Tag 3  # If, elif, else

alter = float(input("Gib dein alter ein:"))

if alter >= 18:   
   print ("Du bist Erwachsen")
else:
    print ("Du bist noch Minderjährig")


zahl = float(input("Geben Sie eine Zahl ein:"))

if zahl > 0:
    print ("Die Zahl ist positiv")
elif zahl < 0:
    print ("Die Zahl ist negativ")
else: 
    print (" Die Zahl ist null")
 
#Tag 4  #range

for i in range (100, -1, -5):
    print(i) 

#Tag 5  #Schleifen

Brands = ["Open Ai", "Anthropic"]
Films = [ "MamaMIA" , "Seven" ]

for film in Films:
   
   print(film)

for brand in Brands:

    print(brand)

#Tag 6  #Dictionaries 

vokabeln = {"Blume":  "Flower", "Auto": "Car", "Tisch": "Desk", "Turm": "Tower", "Katze": "Cat"}

wort= input("Was ist das Wort? ")

if wort in vokabeln: 
   print (vokabeln[wort]) 
else: 
    print(" Wort nicht gefunden!")





for deutsch, englisch  in vokabeln.items():
    print ( deutsch , englisch)

#Tag 7 



