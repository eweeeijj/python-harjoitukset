import math

while True: 
    luku = int(input("Anna luku: "))

    if luku == 0:
        break

    if luku < 0:
        print("Virheellinen numero!")
    else:
        neliojuuri = math.sqrt(luku)
    print(f"Luvun neliöjuuri on {neliojuuri}")
