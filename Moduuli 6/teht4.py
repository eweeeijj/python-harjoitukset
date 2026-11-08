def laske_summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa

testilista = [4, 12, 7, 25, 2, 43]
tulos = laske_summa(testilista)

print(f"Listan {testilista} summa on: {tulos}.")