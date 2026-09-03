# Tag 11: Eine gespeicherte Einkaufsliste aus einer Datei lesen




with open ("einkaufsliste.txt", "r", encoding= "utf-8")as datei:
    produkte = datei.readlines()



for produkt in produkte:
    print(produkt.strip())
