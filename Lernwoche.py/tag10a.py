# Tag 10: Zahleneingaben prüfen und gerade Zahlen sammeln

def istGerade(zahl):
    return zahl % 2 == 0

liste = []

while True:
    try:
        variable = int(input("Geben Sie eine Zahl ein:"))
    except ValueError:
        print("Bitte eine ganze Zahl eingeben")
        continue

    if variable == 0:
        break

    liste.append(variable)

    if istGerade(variable):
        print("Die Zahl ist gerade")
    else:
        print("Die Zahl ist ungerade")
