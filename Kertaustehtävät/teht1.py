tuntipalkka = float(input("Anna tuntipalkka: "))
tunnit = float(input("Anna tehdyt työtunnit: "))
viikonpaiva = input("Anna viikonpäivä: ")

if viikonpaiva == "sunnuntai":
    palkka = (tuntipalkka *2) * tunnit

else:
    palkka = tuntipalkka * tunnit

print(f"Päivä palkka on: {palkka:.2f} euroa.")