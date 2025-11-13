#opdracht: Maak blackjack
#djordy
#07-10-2025
#Deze code is een module voor blackjack.py maakt classes: speler, deler en kaart 

#dit is voor de hoofd progamma van blackjack.py
import random

class Kaart:
    def __init__(self, naam, waarde):
        self.naam = naam
        self.waarde = waarde

    def info(self):
        return self.naam, self.waarde

class Deler:
    def __init__(self):
        self.hand = []
    
    def voeg_toe(self, kaart):
        self.hand.append(kaart)
    
    def laat_zien(self):
        for kaart in self.hand:
            kaart, waarde = kaart.info()
            print(f"de kaart is een: {kaart} en heeft een waarde van: {waarde}")

class Speler:
    def __init__(self):
        self.hand = []

    def voeg_toe(self, kaart):
        self.hand.append(kaart)
    
    def laat_zien(self):
        for kaart in self.hand:
            kaart, waarde = kaart.info()
            print(f"de kaart is een: {kaart} en heeft een waarde van: {waarde}")

#Lijst van kaarten
kaarten = []
gepopte_kaarten = []

#append data
#Schoppen
#unicode \u2660
kaarten.append(Kaart("\u2660 2", 2))
kaarten.append(Kaart("\u2660 3", 3))
kaarten.append(Kaart("\u2660 4", 4))
kaarten.append(Kaart("\u2660 5", 5))
kaarten.append(Kaart("\u2660 6", 6))
kaarten.append(Kaart("\u2660 7", 7))
kaarten.append(Kaart("\u2660 8", 8))
kaarten.append(Kaart("\u2660 9", 9))
kaarten.append(Kaart("\u2660 10", 10))
kaarten.append(Kaart("\u2660 Boer", 10))
kaarten.append(Kaart("\u2660 Vrouw", 10))
kaarten.append(Kaart("\u2660 Heer", 10))
kaarten.append(Kaart("\u2660 Aas", 10))
#Harten
#unicode \u2665
kaarten.append(Kaart("\u2665 2", 2))
kaarten.append(Kaart("\u2665 3", 3))
kaarten.append(Kaart("\u2665 4", 4))
kaarten.append(Kaart("\u2665 5", 5))
kaarten.append(Kaart("\u2665 6", 6))
kaarten.append(Kaart("\u2665 7", 7))
kaarten.append(Kaart("\u2665 8", 8))
kaarten.append(Kaart("\u2665 9", 9))
kaarten.append(Kaart("\u2665 10", 10))
kaarten.append(Kaart("\u2665 Boer", 10))
kaarten.append(Kaart("\u2665 Vrouw", 10))
kaarten.append(Kaart("\u2665 Heer", 10))
kaarten.append(Kaart("\u2665 Aas", 10))
#Klaveren
#unicode \u2663
kaarten.append(Kaart("\u2663 2", 2))
kaarten.append(Kaart("\u2663 3", 3))
kaarten.append(Kaart("\u2663 4", 4))
kaarten.append(Kaart("\u2663 5", 5))
kaarten.append(Kaart("\u2663 6", 6))
kaarten.append(Kaart("\u2663 7", 7))
kaarten.append(Kaart("\u2663 8", 8))
kaarten.append(Kaart("\u2663 9", 9))
kaarten.append(Kaart("\u2663 10", 10))
kaarten.append(Kaart("\u2663 Boer", 10))
kaarten.append(Kaart("\u2663 Vrouw", 10))
kaarten.append(Kaart("\u2663 Heer", 10))
kaarten.append(Kaart("\u2663 Aas", 10))
#Ruiten
#unicode \u2666
kaarten.append(Kaart("\u2666 2", 2))
kaarten.append(Kaart("\u2666 3", 3))
kaarten.append(Kaart("\u2666 4", 4))
kaarten.append(Kaart("\u2666 5", 5))
kaarten.append(Kaart("\u2666 6", 6))
kaarten.append(Kaart("\u2666 7", 7))
kaarten.append(Kaart("\u2666 8", 8))
kaarten.append(Kaart("\u2666 9", 9))
kaarten.append(Kaart("\u2666 10", 10))
kaarten.append(Kaart("\u2666 Boer", 10))
kaarten.append(Kaart("\u2666 Vrouw", 10))
kaarten.append(Kaart("\u2666 Heer", 10))
kaarten.append(Kaart("\u2666 Aas", 10))

#shuffle kaarten
random.shuffle(kaarten)

if kaarten == []:
    kaarten.append(gepopte_kaarten)