print("Hello you!, ik ben jayden")
naam = input("wat is jouw naam ")
print("Hallo " + naam )
print("ik ben een nieuwkomer op het mediacollege Amsterdam\n door een aantal vragen over mij te beantwoorden leer je mij beter kennen.")
antwoord = input("voor ik op het MBO mediacollege Amsterdam kwam, zat ik op \n A. De Katholieke scholengemeenschap hoofddorp  \n B. Kai Munk \n C. HVC \nWat is het correcte antwoord? A, B of C????\n ")
A = antwoord
if antwoord == "B" or antwoord == "C":
    print("fout") 
else:
    print("Goedzo ik zat op De katholieke scholengemeenschap hoofddorp")
    print("Oke volgende vraag")
    antwoord2 = input ("wat is mijn favoriete eten  \nA. Gebraden spek \nB. kip \nC. Zalm\n ")
    if antwoord2 == "B":
        print("Goedzo")
        antwoord3 = input ("Wat is mijn eerste anime \nA. Naruto \n.B Dragonball   \n.C Magi \n")
        C = antwoord3
        if antwoord3 == "C":
                print("goedzo mijn eerste anime was Magi. Hoe wist je dat?")
        else:
            print("fout")
    else:
        print("Fout")