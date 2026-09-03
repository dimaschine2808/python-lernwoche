# Tag 8: Gerade Zahlen mit einer Funktion erkennen

def ist_gerade(zahl):
    return zahl % 2 == 0

liste = [1,2,3,4,5,]

for zahl in liste:
    if ist_gerade(zahl):
        print(f"{zahl} ist gerade")

    else:
        print(f"{zahl} ist ungerade")





