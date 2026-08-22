def istGerade(zahl):
    return zahl % 2 == 0

GanzZahlen = []
GeradeZahlen = []
UngeradeZahlen = []


while True:
    try:
        variable = int(input("Geben sie ihre Zahl ein:"))
    except ValueError:
        print("Bitte geben Sie ihre ganze Zahl ein")
        continue

    if variable == 0:
        break

    GanzZahlen.append(variable)

    if istGerade(variable):
        GeradeZahlen.append(variable)
    else:
        UngeradeZahlen.append(variable)

print("Alle Zahlen:", GanzZahlen)
print("Gerade Zahlen", GeradeZahlen)
print("Ungerade Zahlen", UngeradeZahlen)
