import sys
import os            

os.system("cls")

intro = False

verhaal = False  

stuk_1 = False
stuk_2 = False  
stuk_3 = False
stuk_4 = False
stuk_5 = False
stuk_6 = False
stuk_7 = False
stuk_8 = False
stuk_9 = False
stuk_10 = False       
stuk_11 = False      
stuk_12 = False
stuk_13 = False       
stuk_14 = False
stuk_15 = False
stuk_16 = False
stuk_17 = False
stuk_18 = False
stuk_19 = False
stuk_20 = False
stuk_21 = False
einde_1 = False
einde_2 = False
einde_3 = False
einde_4 = False
einde_5 = False
einde_6 = False
einde_7 = False
einde_8 = False
einde_9 = False
einde_10 = False
einde_11 = False
einde_12 = False



print("welkom bij het verhaal van satsuut chuhiha.\nSatsuut is een soldaar uit Syrie die wilt vluchten voor de oorlog.\nHij werdt veraden door een andere soldaat in het leger en wordt hierom gezocht voor landverraad.")
print("druk op enter om te beginnen")
start = input()
print("")

verhaal = True
stuk_1 = True

while verhaal == True:

#stuk 1
    while stuk_1 == True:
        os.system("cls")
        print("Je wordt wakker geschud door je vrouw, ze zegt dat er soldaten voor de deur staan.\nOmdat je dit al had vewacht heb je je spullen klaar liggen om gelijk te kunnen vluchten.")
        print("Probeer je te vluchten?\nA. Je vlucht.\nB. Je verstopt je.")
        antwoord_1 = input()

        if antwoord_1 == "A":
            stuk_6 = True
            stuk_1 = False
              

        elif antwoord_1 == "B":
            stuk_1 = False
            stuk_2 = True

        else:
            print("dit antwoord is niet geldig.\nGebruik alstublieft A of B")
#stuk 2
    while stuk_2 == True:
        os.system("cls")
        print("Je wilt je verstoppen maar weet niet waar.\nJe zegt tegen je vrouw dat ze de soldaten nog even buiten moet houden terwijl je een verstop plek zoekt.\waar ga je naar toe")
        print("A. De zolder.\nB. de kelder.")
        antwoord_2 = input()

        if antwoord_2 == "A":
            stuk_3 = True
            stuk_2 = False

        elif antwoord_2 == "B":
            stuk_2 = False
            stuk_5 = True

        else:
            print("dit antwoord is niet geldig.\nGebruik alstublieft A of B")
#stuk 3
    while stuk_3 == True:
        os.system("cls")
        print("Je zit nu op zolder, op zolder staat een oude kist en een oude kast.\nJe weet dat er in de kast en de kist geen spullen zitten.\nOok hoor je de soldaten naar boven lopen.\nWaar ga je je verstoppen")
        print("A. Kist.\nB. Kast")
        antwoord_3 = input()

        if antwoord_3 == "A":
              stuk_4 = True
              stuk_3 = False

        elif antwoord_3 == "B":
            einde_1 = True
            stuk_3 = False

        else:
            print("dit antwoord is niet geldig.\nGebruik alstublieft A of B")
#stuk 4
    while stuk_4 == True:
        os.system("cls")
        print("je springt in de kist voor dat de soldaten boven zijn.\nTijdens je sprong raak je de kast en de kast begint te wiebelen.\nDe soldaten zien dit en kijken in de kast, maar er zit niemand in.\De soldaten zijn kwaad. ze trappen tegen de kist aan maar gaan weer weg.\Waarneer je hun auto's hoort wegrijden kom je uit de kist")
        print("Je pakt de rest van je spullen en gaat weg")
        print("Druk op enter om verder te gaan")
        antwoord_4 = input()

        if antwoord_4 == "":
            stuk_4 = False
            stuk_6 = True
            
#einde_1
    while einde_1 == True:
        os.system("cls")
        print("Je verstopt je in de kast. De soldaten zijn niet dom en lopen naar de kast toe.\nZe grijpen je en je wordt meegenomen in hun auto's")
        print("THE END")
        verhaal = False
        einde_1 = False
        sys.exit()
#stuk_5
    while stuk_5 == True:
        os.system("cls")
        print("Je rent de kelder in, je kelder heeft een raam naar buiten.\nBlijf je binnen of ga je naar buiten?.")
        print("A. Je gaat door het raam naar buiten.\nJe blijft binnen.")
        antwooord_5 = input()

        if antwoord_5 == "A":
            stuk_6 = True
            stuk_5 = False

        elif antwoord_5 == "B":
            stuk_5 = False
            einde_2 = True

        else:
            print("dit antwoord is niet geldig.\nGebruik alstublieft A of B")
#einde 2
    while einde_2 == True:
        os.system("cls")
        print("Je blijft in de kelder met geen andere uitweg, de soldaten lopen naar beneden.\Je slaat een soldaat neer, maar de andere soldaten pakken je en nemen je mee")
        print("THE END")
        verhaal = False
        einde_2 = False
        sys.exit
#stuk_6
    while stuk_6 == True:
        os.system("cls")
        print("Je rent weg naar buiten, er is een groot bebost stuk achter je huis.\nJe weet dat 1 van je vrienden met smokkelaars maar het kan gevaarlijk zijn om hem op te zoeken.\n zoek je hem op of niet")
        print("A. Ga naar hem toe.\nB. Ga zelf op pad.")
        antwoord_6 = input()

        if antwoord_6 == "A":
            stuk_6 = False
            stuk_17 = True

        elif antwoord_6 == "B":
            stuk_6 = False
            stuk_7 = True

        else:
            print("dit antwoord is niet geldig.\nGebruik alstublieft A of B")
#stuk_7
    while stuk_7 == True:
        os.system("cls")
        print("Je loopt door het bos heen en komt bij een snelweg aan.\n Je loopt langs de weg met je duim omhoog om te kijken of je met iemand mee kan liften.\nEr stopt een rode auto en een man en vrouw vragen of je mee wilt liften.")
        print("Je lift mee tot aan in Damascus, de hoofdstad en zoekt een bar om uit te rusten.\nIn de bar hoor je mensen praten over mensensmokkelaars.\Je loopt naar de mensen toe en vraagt erover.\nZe vragen aan je om mee te gaan als je meer wilt weten.")
        print("Ga je met ze mee?")
        print("A. Ja, ga mee.\nB. blijf in de bar en praat erover.")
        antwoord_7 = input()

        if antwoord_7 == "A":
            stuk_7 = False
            stuk_8 = True

        elif antwoord_7 =="B":
            stuk_7 = False
            einde_3 = True

        else:
            print("dit antwoord is niet geldig.\nGebruik alstublieft A of B")
#einde_3
    while einde_3 == True:
        os.system("cls")
        print("Je blijft in de bar en praat over de smokkeling, mensen om jullie heen horen jullie en bellen zonder dat jullie het horen de politie.\nBinnen 5 minuten is de politie er en worden jij en de smokkelaars opgepakt")
        print("THE END")
        verhaal = False
        einde_3 = False
        sys.exit()
#stuk_8
    while stuk_8 == True:
        os.system("cls")
        print("De groep betalen met zijn allen en lopen naar buiten.\n Jullie lopen een steeg in en de mannen beginnen te vragen waarom je wilt weten of de Smokkelingen.\nOok al vertrouw je de mannen niet echt, vertel je ze toch dat je op de vlucht bent en het land uit wilt")
        print("De mannen zeggen dat je moet mee lopen, je weet niet waar jullie heen gaan maar toch loop je mee.\nJe komt aan bij een verlaten woning.\nHier worden volgens de mannen de smokkelingen gedaan. Na een half uur binnen te zijn en te praten met de mannen, vraag je naar de prijs.\Het is erg duur en meer dan je bij je hebt.\n Wel heb je nog je trouwring die genoeg waard is.")
        print("Hoe ga je geld krijgen?")
        print("A. Stelen.\nB. trouwring geven.")
        antwoord_8 = input()
        if antwoord_8 == "A":
            stuk_8 = False
            stuk_9 = True

        elif antwoord_8 == "B":
            stuk_8 = False
            stuk_15 = True
        else:
            print("Dit antwoord is niet geldig.\nGebruik alstublieft A of B")
#stuk_9
    while stuk_9 == True:
        os.system("cls")
        print("Waarneer je zegt dat je iets waardevols wilt gaan stelen, zeggen de smokkelaars dat er een gerucht gaan de is over een kluis in het huis van de burgemeester.\nZe zeggen hierbij dat er veel waardevolle spullen in horen te zitten.")
        print("Waarneer je bij de burgermeester aan komt wordt je gelijk tegen gehouden.\nHet is blijkbaar niet zo makkelijk als gewoon naar binnen lopen.\nWaarneer je om het huis heen loopt zie je een gat in het hek.\nJe kruipt eronder door en bent in de achtertuin.")
        print("Hoe ga je verder?")
        print("A. De achterdeur.\nB. De garageDeur")
        antwoord_9 = input()

        if antwoord_9 == "A":
              stuk_9 = False
              einde_4= True

        elif antwoord_9 == "B":  
            stuk_9 = False
            stuk_10 = True

        else:
            print("Dit antwoord is niet geldig.\nGebruik alstublieft A of B")
#einde_4
    while einde_4 == True:
        os.system("cls")
        print("Je opent de achterdeur. Je staat nu oog in oog met een bewaker.\nDe bewaker grijpt je vast en arresteerd je")
        print("THE END")
        verhaal = False
        einde_4 = False
        sys.exit()
        
#stuk_10
    while stuk_10 == True:
        os.system("cls")
        print("Je gaat via de GarageDeur naar binnen in. Je ziet een bewaker naar beneden lopen.\nWaarneer hij de keuken in gaat ren je snel naar boven.\nWaar ga je zoeken voor de kluis?")
        print("A.Slaapkamer.\nB. Kantoor.")
        antwoord_10 = input()
        if antwoord_10 == "A":
            stuk_10 = False
            stuk_11 = True

        elif antwoord_10 =="B":
            stuk_10 = False
            stuk_14 = True

        else:
           print("Dit antwoord is niet geldig.\nGebruik alstublieft A of B")
#stuk_11
    while stuk_11 == True:
        os.system("cls")
        print("Je rent naar de slaapkamer om te kijken of er iets te vinden is.\nJe kijkt eerst in de nachtkastjes maar hoort iemand aan komen")
        print("Waar verstop je je?")
        print("A. De Kledingkast.\nB. Onder het bed.")
        antwoord_11 = input()

        if antwoord_11 == "A":
            stuk_11 = False
            stuk_12 = True

        elif antwoord_11 =="B":
            stuk_11 = False
            einde_5 = True

        else:
           print("Dit antwoord is niet geldig.\nGebruik alstublieft A of B")
#einde_5
    while einde_5 == True:
        os.system("cls")
        print("Je probeert je onder het bed te verstoppen, Jammer genoeg is het bed te laag en kan je er niet onder kruipen.\nJe wordt gearresteerd.")
        print("THE END")
        verhaal = False
        einde_5 = False
        sys.exit()
#stuk_12
    while stuk_12 == True:
        os.system("cls")
        print("Je verstopt je in de kast, waarneer je in de kast zit voel je iets in je rug prikken.\nEr zit een hendel in kast, Waarneer je aan de hendel trekt gaat een deel van de kast open.\nJe loopt erin en je bevindt je nu in de kluis.\n Je pakt alle sieraden en waardevolle spullen die je kan.")
        print("Nu moet je alleen nog naar buiten kunnen komen zonder gepakt te worden.\nJe ziet een ventitlatie schacht, maar je kan ook via de Kast weer naar buiten.")
        print("Hoe ga je naar buiten?")
        print("A. Via de kast.\nB. Via de ventilatie.")
        antwoord_12 = input()

        if antwoord_12 == "A":
            stuk_12 = False
            einde_6 = True

        elif antwoord_12 == "B":
            stuk_12 = False
            stuk_13 = True
        
#einde_6
    while einde_6 == True:
        os.system("cls")
        print("Je loopt de kast uit en staat nu oog in oog met een bewaker.\nJe wordt gearresteerd")
        print("THE END")
        verhaal = False
        einde_6 = False
        sys.exit()
#stuk_13
    while stuk_13 == True:
        os.system("cls")
        print("Je kruipt de ventilatie schacht in. De schacht komt uit in de buurt van het gat in het hek.\nJe klimt onder het hek door en rent zo snel mogelijk weg.")
        print("Na een tijd rennen kom je aan bij de schuilplek van de smokkelaars.\nJe laat ze de sieraden zien en ze zeggen dat dit genoeg is voor de smokkeling en dat je 2 Weken moet wachten jullie vertrekken")
        print("Er gaan twee weken voorbij en 1 van de smokkelaars geeft je een nep paspoort en jullie stappen met zijn allen een busje in.")
        antwoord_13 = input()
        if antwoord_13 == "":
            stuk_16 = True
            stuk_13 = False
#stuk_14
    while stuk_14 == True:
        os.system("cls")
        print("Je rent naar het kantoor.\n Je kijkt door alle kastjes en laatjes en vind een trouwring.\nOmdat je niet langer wilt blijven klim je uit het raam.\nJe gaat door het gat in het naar buiten en rent zo snel mogelijk weg")
        print("Na een tijd rennen kom je aan bij de schuilplek van de smokkelaars.\nJe laat ze de sieraden zien en ze zeggen dat dit genoeg is voor de smokkeling en dat je 2 Weken moet wachten jullie vertrekken")
        print("Er gaan twee weken voorbij en 1 van de smokkelaars geeft je een nep paspoort en jullie stappen met zijn allen een busje in.")
        print("Druk op Enter om door te gaan")
        antwoord_14 = input()
        if antwoord_14 == "":
            stuk_16 = True
            stuk_14 = False

#stuk_15
    while stuk_15 == True:
        os.system("cls")
        print("Je geeft de smokkelaars je trouwring.\nYour wife will remember that")
        print("Hij was veel waard, dus het was genoeg voor de smokkeling. Ze zeggen dat je 2 Weken moet wachten jullie vertrekken")
        print("Er gaan twee weken voorbij en 1 van de smokkelaars geeft je een nep paspoort en jullie stappen met zijn allen een busje in.")
        print("Druk op Enter om door te gaan")
        antwoord_15 = input()

        if antwoord_15 == "":
            stuk_16 = True
            stuk_15 = False
#stuk_16
    while stuk_16 == True:
        os.system("cls")
        print("Ze zeggen dat de reis ongeveer de reis ongeveer 4 tot 5 dagen kan duren.\n Onder weg maken jullie nog wat stops maar na 4 dagen komen jullie aan in nederland")
        print("Ze zetten je af voor het gemeentetehuis in amsterdam. Ze zeggen dat je naar binnen moet lopen en dat de rest van zelf gaat.\nJe gaat naar binnen en wordt gelijk tegengehouden door een groep mensen.\nZe praten in het nederlands dus je verstaat ze niet.\n wel heb je een paar woorden geleerd tijdens de reis")
        print("Met moeite zeg je tegen de mensen dat je een vluchteling bent.\nJe wordt gelijk doorgewezen en na een maand krijg je te horen dat je een statushouder geworden bent")
        print("In deze maand ben je gaan studeren zodat je zo snel mogelijk de inburgering kan doen. Ook krijg je een woning toegewezen door de overheid")
        print("Een jaar later doe je de inburgerings examens en haal je ze")
        print("Je bent nu officeel een burger")
        print("THE END")
        verhaal = False
        stuk_16 = False
        sys.exit()
#stuk_17
    while stuk_17 == True:
        os.system("cls")
        print("Je besluit om je vriend op te zoeken.\nJe weet dat hij nog een schuld bij je aftebetalen heeft dus je wilt dit tegen hem gebruiken.\nNa een paar dagen kom je aan in de stad Dera.\nJe belt aan bij je Vriend, Zijn naam is Emir, maar zin vrouw doet open en zegt dat hij tijdelijk weg is.")
        print("Je gaat hem zoeken")
        print("Waar ga je zoeken")
        print("A. Het winkel centrum in de buurt.\B. De bar.")
        antwoord_17 = input()

        if antwoord_17 == "A":
            stuk_17 = False
            stuk_20 = True

        elif antwoord_17 == "B":
            stuk_17 = False
            stuk_18 = True
#stuk_18
    while stuk_18 == True:
        os.system("cls")
        print("Je loopt naar de bar aan de overkant van de straat, Emir is er niet, maar zijn zoon is er wel.\nHij zegt dat zijn vader een half uur geleden naar de bar zou komen maar er nog steeds niet is.\nZijn zoon zegt dat zijn vader wat ging halen in het winkelcentrum met zijn zus.")
        print("Hierna loop je naar het winkelcentrum toe.Terwijl je er heen loopt kom je Emir tegen met zijn dochter.\nJe vraagt hem of hij een afspraak had met zijn zoon, waarop hij antwoordt dat hij hem vergeten was.")
        print("Jullie halen Emir's zoon op bij de bar en gaan naar Emirs huis toe.")
        print("Nu vraagt Emir wat je komt doen")
        print("A. Vraag om hulp\nB. Vraag om onderdak.")
        antwoord_18 = input()

        if antwoord_18 == "A":
            stuk_18 = False
            stuk_19 = True

        elif antwoord_18 == "B":
            stuk_18 = False
            stuk_21 = True
#stuk_19
    while stuk_19 == True:
        print("Je vraagt Emir of hij je kan helpen met de vucht van het leger.\nHij zegt tegen je dat hij je kan helpen, maar dit ook gelijk zijn schulde bij je afbetaald")
        print("Hier had je al op gerekened dus dit vind je geen probleem.\nHij zegt dat het ongeveer een week zal duren voor jullie vertrekken en dat je tot die tijd in de kelder moet slapen.")
        print("Na een week wachten stap je bij een groep smokkelaars een bus in en beginnen julie te rijden.")
        print("Druk op Enter om door te gaan")
        antwoord_19 = input()

        if antwoord_19 == "":
            stuk_19 = False
            stuk_20 = True
#stuk_20
    while stuk_20 == True:
        os.system("cls")
        print("Ze zeggen dat de reis ongeveer de reis ongeveer 4 tot 5 dagen kan duren.\n Onder weg maken jullie nog wat stops maar na 4 dagen komen jullie aan in nederland")
        print("Ze zetten je af voor het gemeentetehuis in amsterdam. Ze zeggen dat je naar binnen moet lopen en dat de rest van zelf gaat.\nJe gaat naar binnen en wordt gelijk tegengehouden door een groep mensen.\nZe praten in het nederlands dus je verstaat ze niet.\n wel heb je een paar woorden geleerd tijdens de reis")
        print("Met moeite zeg je tegen de mensen dat je een vluchteling bent.\nJe wordt gelijk doorgewezen en na een maand krijg je te horen dat je een statushouder geworden bent")
        print("In deze maand ben je gaan studeren zodat je zo snel mogelijk de inburgering kan doen. Ook krijg je een woning toegewezen door de overheid")
        print("Een jaar later doe je de inburgerings examens en haal je ze")
        print("Je bent nu officeel een burger")
        print("THE END")
        verhaal = False
        stuk_20 = False
        sys.exit()
#stuk_21
    while stuk_21 == True:
        print("Je vraagt aan Emir of hij onderdak voor je zou kunnen regelen. Hierop zegt hij dat hij een aantal mensen kent die in een afgelegen gebied leven.\nJullie gaan hier een kijkje nemen en het ziet er beter uit dan je had verwacht. meeste dingen worden er zelf verbouwt zoals groenten en vlees dus je hoeft niet vaak het dorp uit")
        print("Een week later verhuizen jij en je vrouw naar een huis in het dorpje en leven erg gelukkig")
        print("THE END")
        verhaal = False
        stuk_21 = False
        sys.exit()
    
        
        

        
            
            
        
    
