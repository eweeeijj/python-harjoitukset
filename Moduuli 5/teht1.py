##Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. 
##Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. 
##Käytä fortoistorakennetta.
import random

arpakuutiot = int(input("Kerro arpakuutioiden määrä: "))
summa = 0

for i in range(arpakuutiot):
    luku = random.randint (1, 6)
    print(luku)
    summa += luku

print("Lukujen summa on;" ,summa)

