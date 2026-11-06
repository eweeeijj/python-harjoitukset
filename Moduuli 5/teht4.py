kaupungit = []

for i in range(5):
    kaupunki = input(f"Anna {i+1}. kaupunki: ")
    kaupungit.append(kaupunki)

print("\nKaupungit ovat: ")

for kaupunki in kaupungit:
    print(kaupunki)
    