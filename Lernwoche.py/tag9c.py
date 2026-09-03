# Tag 9: Notengruppen mit verschachtelten Schleifen auswerten

noten_gruppen = [
    [1, 3, 5],
    [2, 6, 0],
    [4, 7, 2]
]




for gruppe in noten_gruppen:
    print("gesamte Gruppe")

    for note in gruppe:
        print("----------")

    

        if 1 <= note <= 6:
            if note > 4: 
                print(f"{note} nicht bestanden")
            else:
                print(f"{note} bestanden")
        else:
            print(f"{note} ungueltige Note")
        
        
