# Tag 8: Zahlen mit einer Funktion einordnen

def ist_GerOderUng(zahl):
  

    return zahl % 2 == 0


zahlen = [-4, 7, 0, 12, -9]


for zahl in zahlen:
    if zahl > 0:
        if ist_GerOderUng(zahl):
            print (f"{zahl} ist positiv und gerade")
        else:
            print (f"{zahl} ist postiv und ungerade")
    elif zahl < 0:
        print (f"{zahl} ist negativ")

    else:
        print(f"{zahl} ist Null")



