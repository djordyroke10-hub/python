#opdracht: bouw je eige rekenmachine
#djordy
#10-09-2025
#deze code zal een rekenmeachine zijn

#importeren van de module genaamd berekeningen (het bestand berekeningen.py hier zitten berekenings functies in)
import berekeningen

#checken of het echt nummers zijn die de gebruiker invoert
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ongeldige invoer. Voer een geldig getal in.") #je heb geen nummer ingevoert

#welke berekeningen word er aan gevraagd
def get_berekening_input():
    opties = ["optellen", "aftrekken", "vermenigvuldigen", "delen"] #deze optie kan je uit kiezen
    while True:
        keuze = input("Welke berekening wil je doen? (optellen, aftrekken, vermenigvuldigen, delen): ").lower()
        if keuze in opties:
            return keuze #geeft de optie terug 
        else:
            print("Ongeldige keuze. Kies uit optellen, aftrekken, vermenigvuldigen of delen.") #er is iets verkeerd gegeaan bij de invoer

while True:
    #gebruikers invoer
    input_berekening = get_berekening_input()   #welke berekening wil je doen?
    input_getal1 = get_float_input("Voer het eerste getal in: ") #eerste getal
    input_getal2 = get_float_input("voer het tweede getal in: ") #tweede getal

    #uitvoeren van de juiste berekening
    if input_berekening == "optellen": #als je voor optellen heb gekozen
        resultaat = berekeningen.optellen(input_getal1, input_getal2)
        print(f"Het resultaat van {input_getal1} + {input_getal2} is {resultaat}")

    elif input_berekening == "aftrekken": #als je voor aftrekken heb gekozen
        resultaat = berekeningen.aftrekken(input_getal1, input_getal2)
        print(f"Het resultaat van {input_getal1} - {input_getal2} is {resultaat}")

    elif input_berekening == "vermenigvuldigen": #als je voor vermenigvuldigen heb gekozen
        resultaat = berekeningen.vermenigvuldigen(input_getal1, input_getal2)
        print(f"Het resultaat van {input_getal1} * {input_getal2} is {resultaat}")

    elif input_berekening == "delen": #als je voor delen heb gekozen
        resultaat = berekeningen.delen(input_getal1, input_getal2)
        #controle voor delen door nul
        if resultaat == "Fout: Delen door nul is niet toegestaan.": #probeerde door nul te delen
            print(resultaat)
        else:
            print(f"Het resultaat van {input_getal1} / {input_getal2} is {resultaat}")

    else: #er isiets mis gegaan
        print("Ongeldige berekening. Kies uit optellen, aftrekken, vermenigvuldigen of delen.") #er is iets totaal mis gegaan hoe kom je zelfs hier wat!!

    #vragen of de gebruiker nog een berekening wilt doen
    opnieuw = input("Wil je nog een berekening doen? (ja/nee): ").strip().lower()
    if opnieuw != "ja": #waneer opnieuw niet ja is
        print("Programma gestopt.")
        break #einde progamma