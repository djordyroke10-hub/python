#Importeeren van de kaarten speler en deler
import spel_onderdelen
import os

#Berekenen van de waarde in de hand
def bereken_hand_waarde(hand):
    totaal = 0
    aas_count = 0

    #Bereken alle kaarten in de hand
    for kaart in hand:
        if "Aas" in kaart.naam:
            aas_count += 1
            totaal += 11
        else:
            totaal += kaart.waarde

    #Als de totaal boveb 21 is zet de aas naar 1
    while totaal > 21 and aas_count > 0:
        totaal -= 10
        aas_count -= 1

    return totaal

#Deel kaarten uit aan de speler of deler
def deel_kaart(deler_of_speler, is_speler = False, is_deler = False):
    #maak een kaart aan
    kaart = spel_onderdelen.kaarten.pop(0)

    # Vraag alleen bij speler om waarde van een Aas 1 of 11
    if is_speler and "Aas" in kaart.naam:
        # tijdelijk toevoegen van kaart met waarde 11 om handwaarde te berekenen
        kaart.waarde = 11
        tijdelijk_hand = deler_of_speler.hand + [kaart]
        totaal = bereken_hand_waarde(tijdelijk_hand)

        #Als de handwaarde precies 21 is met deze Aas, zet waarde van Aas automatisch naar 1
        if totaal == 21:
            kaart.waarde = 1
        else:
            while True:  #Alleen wanneer je een aas hebt en handwaarde is niet 21
                keuze = input(f"\nJe hebt een Aas gekregen ({kaart.naam})! Wil je dat deze 1 of 11 waard is? (voer 1 of 11 in): ")
                if keuze == "1":  #Zet de kaart waarde naar 1
                    kaart.waarde = 1
                    break
                elif keuze == "11":  #Zet de kaart waarde naar 11
                    kaart.waarde = 11
                    break
                else:
                    print("Ongeldige invoer, probeer opnieuw.")  #Foute invoer

        #Kijk naar de azen die de deler heeft
        if is_deler and "Aas" in kaart.naam:
            #Teidelijk toevoegen van de kaart
            kaart.waarde = 11
            tijdelijk_hand = deler_of_speler.hand + [kaart]
            totaal = bereken_hand_waarde(tijdelijk_hand)

            #Als de totaal gelijk is aan 21 zet de kaart waarde naar 1
            if totaal == 21:
                kaart.waarde = 1
            else:
                kaart.waarde = 11

    deler_of_speler.voeg_toe(kaart)  #Voeg kaart toe aan speler of deler
    spel_onderdelen.gepopte_kaarten.append(kaart)  #Zet de gepopte kaart in een array
    return kaart  #Keert kaart terug

#Print gespeelde hand
def print_hand(speler_of_deler, naam): #Is het de hand van speler of deler?
    print(f"\n########################\n{naam} heeft de volgende kaarten:\n")

    #Print elke kaart in de hand
    for kaart in speler_of_deler.hand:
        print(f"{kaart.naam}")

    #Print de totaal berekende waarde van de kaarten
    totaal = bereken_hand_waarde(speler_of_deler.hand)
    print(f"------------------------\nTotaal: {totaal}\n########################\n")

#Blackjacken
def main():
    #Maak de speler en de deler aan
    deler = spel_onderdelen.Deler()
    speler = spel_onderdelen.Speler()

    #Geef 2 kaarten aan iedereen
    for _ in range(2):
        deel_kaart(deler, is_deler = True)
        deel_kaart(speler, is_speler = True)

    #Print ieders hand
    print_hand(speler, "Speler")
    print_hand(deler, "Deler")

    #Spelers beurt
    while True:

        #Als je score presies 21 is. Heb je automatich gewonnen
        totaal = bereken_hand_waarde(speler.hand)
        if totaal == 21:
            print("Je heb presies 21. je heb gewonnen")
            return
        
        #Maak keuze Hit of CALL
        try:
            keuze = int(input("1) HIT\n2) CALL\n> "))
        except ValueError:
            print("Ongeldige invoer, probeer het opnieuw.")
            continue

        if keuze == 1:  #HIT (nog een kaart pakken)
            #Deel nog een kaart uit
            kaart = deel_kaart(speler, is_speler=True)
            print(f"\n########################\nJe kreeg: {kaart.naam}")

            #Print de neiuwe  totaal waarde
            totaal = bereken_hand_waarde(speler.hand)
            print(f"------------------------\nJe totaal is nu: {totaal}\n########################\n")
            

            #Als de totaal boven 21 is verlies je
            if totaal > 21:
                print("\nJe bent over 21 gegaan. Je verliest!")
                return
            else:
                break #Einde van je beurt
        elif keuze == 2:  # CALL (einde van de beurt)
            break
        else:
            print("Ongeldige invoer, probeer het opnieuw.") #foute invoer

    #Delers beurt
    print_hand(deler, "Deler")

    #Als de delers hand onder de 17 is zal hij nog een kaart pakken
    while bereken_hand_waarde(deler.hand) < 17:

        #deel nog een kaart uit
        kaart = deel_kaart(deler, is_deler = True)
        print(f"\n########################\nDe deler pakt: {kaart.naam}")

        #print het neiuwe totaal uit
        totaal = bereken_hand_waarde(deler.hand)
        print(f"------------------------\nHet totaal van de deler is nu: {totaal}\n########################\n")
        break

    #Uitslag bepalen
    speler_totaal = bereken_hand_waarde(speler.hand)
    deler_totaal = bereken_hand_waarde(deler.hand)

    if deler_totaal > 21:
        print("\nDeler is over de 21. Jij hebt gewonnen!!")
    elif speler_totaal == 21:
        print("\njou totaal is 21. je heb gewonnen")
    elif speler_totaal > deler_totaal:
        print("\nGefeliciteerd jou tataal is kleiner dan die van de deler, jij hebt gewonnen!")
    elif speler_totaal == deler_totaal:
        print("\nGelijkspel!")
    else:
        print("\nJij hebt verloren!")

#Als de __naam__ __main__ is, doe deze condities
if __name__ == "__main__":
    while True:
        try:
            #maak een keuze en de uitleg van het spel
            uitleg = int(input(
                "\nUitleg:\n\n"
                "Het doel van het spel is de bank (deler) te verslaan.\n"
                "Hierbij moet men proberen dichter bij de 21 punten te komen dan de bank.\n"
                "Als de speler boven de 21 punten uitkomt heeft hij verloren, ongeacht wat de bank heeft.\n\n"
                "1. Speel blackjack\n"
                "2. Spel afsluiten\n"
                "\n> "
            ))
        except ValueError:  # verkeerde invoer
            print("Ongeldige invoer, probeer het opnieuw.")
            continue

        if uitleg == 1:  # speel het spel
            print("\nWij gaan nu blackjack spelen\n")
            if os.name == 'nt':
                os.system('cls')
            main()
        elif uitleg == 2:  # eindig het spel
            print("\nSpel aan het stoppen\n")
            if os.name == 'nt':
                os.system('cls')
            break
        else:  # verkeerde invoer
            print("Ongeldige keuze, probeer het opnieuw.")