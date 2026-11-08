luvut = []

while True: 
    syote = int(input("Anna luku listaan: "))

    if syote == 0:
        print("Lista lopettu.")
        break

    luvut.append(syote)

    print(f"Lista: {luvut}")
    print(f"Lista järjestyksessä: {sorted(luvut)}")
    print("-" * 30)
    