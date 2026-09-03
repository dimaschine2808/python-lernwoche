# Tag 7: Noten validieren, sammeln und auswerten

Noten = []

#Zeugnisausgabe

while True: 
    Zeugnis = int(input("Gebe bitte deine Note ein:"))
    if Zeugnis == 0: 
        print("Geben Sie ihre Note erneut ein")
        break
    elif 1 <= Zeugnis <= 6:
        print ("Danke fuer die Note") 
        Noten.append(Zeugnis)
    else:
        print ("Note ist ungultig") 
   
      
    print (Noten)


print(f"Minimum: {min(Noten)}")
print(f"Maximum: {max(Noten)}")
print(f"Durchschnitt: {sum(Noten)  / len(Noten)}")
       


