## Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon.
## Lopuksi ohjelma saaduista luvuista viisi suurina suuruusjärjestyksessä suurimmasta alkaen. 
luvut = []

syote = input("Anna luku: ")

while syote != "": 
    luku = int(syote)
    luvut.append(luku)
    syote = input("Anna luku: ")

luvut.sort(reverse=True)

print("Luvut järjestyksessä suurimmasta alkaen: ", luvut[:5])




