# Tag 7: Zahlen sammeln und statistisch auswerten

zahl = []

while True:
    variable = int(input("Gebe deine Zahl ein:"))
    if variable == -1:
        break 
    zahl.append(variable)
    print ("Die Zahl wurde hinzugefuegt")

    print(zahl)

print(f"Summe: {sum(zahl)}")
print(f"Maximum: {max(zahl)}")
print(f"lenght: {len(zahl)}")
print(f"Minumum: {min(zahl)}")

