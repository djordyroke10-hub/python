#opdracht: bouw je eige rekenmachine
#djordy
#10-09-2025
#deze code zal onder deel van een rekenmeachine zijn

#berekening functies
def optellen(a, b): #optellen functie
    return a + b

def aftrekken(a, b): #aftrekken functie
    return a - b

def vermenigvuldigen(a, b): #vermenigvuldigen functie
    return a * b

def delen(a, b): #delen functie
    if a == 0 or b == 0:
        return "Fout: Delen door nul is niet toegestaan." #je kan niet delen door nul
    else:
        return a / b 