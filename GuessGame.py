import random # Der Computer wählt eine zufällige Zahl zwischen 1 und 100
geheime_zahl = random.randint(1, 100)
versuche = 0
print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Kannst du sie erraten?")
while True: 
    tipp = int(input("Dein Tipp: "))
    versuche += 1
    if tipp < geheime_zahl:
        print("Zu niedrig! Versuch es noch einmal.")
    elif tipp > geheime_zahl:
        print("Zu hoch! Versuch es noch einmal.")
    else:
        print(f"Glückwunsch! Du hast die Zahl erraten. Sie war {geheime_zahl}.")
        print(f"Du hast {versuche} Versuche gebraucht.")
        break # Spiel beenden, wenn die Zahl erraten wurde