# Tag 9: Verschachtelte Listen durchlaufen und Zahlen einordnen

gruppen = [
    [4, -3, 0],
    [7, -8, 12],
    [-5, 2, 9]
]

# Eine einzelne Zahl als gerade oder ungerade ausgeben
def geradeORungerade(zahl):

    return zahl % 2 == 0 


for gruppe in gruppen :
    print("Neue Gruppe")

    for zahl in gruppe:
       


        if zahl > 0: 
            if geradeORungerade(zahl):
                print(f"{zahl} ist gerade und positiv")
            else:
                print(f"{zahl} ist positiv und ungerade")
        elif zahl < 0:
            print(f"{zahl} ist negativ") 
        else:
            print(f"{zahl} ist Null")

         

