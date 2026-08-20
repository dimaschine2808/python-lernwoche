liste = ["Apfel", "Birne", "Brot"]

while True: 
  variable = input("Welches produkt möchtest du?") 
  if variable == "fertig":
   break
  liste.append(variable)
  print(variable, "wurde hinzugefuegt")

print(liste)