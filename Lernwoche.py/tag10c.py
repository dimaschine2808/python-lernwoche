# Tag 10: Noteneingaben prüfen und die Liste auswerten

Noten = []

#Zeugnisausgabe

while True:
    try:
        Zeugnis = int(input("Gebe bitte deine Note ein:"))
    except ValueError:
        print("Geben Sie ihre Zahl ein:")
        continue

    if Zeugnis == 0:
        break
    elif 1 <= Zeugnis <= 6:
        print ("Danke fuer die Note")
        Noten.append(Zeugnis)
    else:
        print ("Note ist ungultig")

if len(Noten) > 0:
    print("Noten:", Noten)
    print(f"Minimum: {min(Noten)}")
    print(f"Maximum: {max(Noten)}")
    print(f"Durchschnitt: {sum(Noten) / len(Noten):.1f}")
else:
    print("Es wurden keine Noten eingegeben")
