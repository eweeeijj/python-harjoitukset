luku = int(input("Anna kokonaisluku: "))

if luku % 3 == 0 and luku % 5 == 0:
    print("Luku on jaollinen molemmilla luvuilla!")
elif luku % 3 == 0:
    print("Luku on jaollinen kolmella!")
elif luku % 5 == 0:
    print("Luku on jaollinen viidellä!")
    