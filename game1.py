import random 
def kampf():
    spieler_hp = 20 
    monster_hp = 15
    print("\n EIN WILES MONSTER ERSCHEINT (15 HP)")
    while spieler_hp > 0 and monster_hp > 0:
        print(f"\nDeine HP: {spieler_hp} | Monster HP: {monster_hp}")
        aktion = input("Wähle deine Aktion (angreifen / heilen): ").lower()
        if aktion == "angreifen":
            schaden = random.randint(3, 6)
            monster_hp -= schaden
            print(f"Du greifst das Monster an und verursachst {schaden} Schaden!")
        elif aktion == "heilen":
            heilung = random.randint(2, 5)
            spieler_hp += heilung
            print(f"Du heilst dich um {heilung} HP!")
        else:
            print("Ungültige Aktion. Bitte wähle 'angreifen' oder 'heilen'.")
            continue
        if monster_hp > 0:
            monster_schaden = random.randint(2, 5)
            spieler_hp -= monster_schaden
            print(f"Das Monster greift zurück und verursacht {monster_schaden} Schaden!")
            if spieler_hp <= 0:
                print("Du wurdest besiegt!")
                break
    else:
        print("Das Monster wurde besiegt!")
# Hauptprogramm
print("=== Willkommen zum Kampfspiel! ===")
name = input("Gib deinen Namen ein: ")
print(f"Hallo {name}! Dein Abenteuer beginnt jetzt.")
kampf()

    
       
