


with open ("einkaufsliste.txt", "r", encoding= "utf-8")as datei:
    produkte = datei.readlines()



for produkt in produkte:
    print(produkt.strip())