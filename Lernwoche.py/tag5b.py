# Tag 5: Einen neuen Eintrag an eine Liste anhängen

Filme = ["Matrix", "Inception", "Interstellar"]


neuer_film = input("Gib einen neuen Film ein: ")
Filme.append(neuer_film)

for film in Filme:
    print(film)
