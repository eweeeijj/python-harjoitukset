tuotteet = []
maarat = []

while True: 
    tuote = input("Mitä tuotetta valmistetaan? ")
    maara = int(input("Kuinka monta tuotetta valmistetaan? "))

    tuotteet.append(tuote)
    maarat.append(maara)

    jatketaanko = input("Jatketaanko tuotantoa? ")
    if jatketaanko.strip().lower() == "ei":
        break

print("\nTuotanto lopetettu!")
print("Valmistetut tuotteet:")

for i in range(len(tuotteet)):
    print(f"{tuoteet[i]}: {maarat[i]} kpl")
