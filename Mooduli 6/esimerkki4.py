def neliosumma(eka, toka):
    ns = eka **2 + toka **2
    return ns 

#PÄÄOHJELMA
luku1 = float(input("Anna eka luku: "))
luku2 = float(input("Anna toka luku: "))

tulos = neliosumma(luku1, luku2)

print(f"Lukujen neliösumma on: {tulos:.2f}")