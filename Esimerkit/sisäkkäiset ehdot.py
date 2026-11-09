numero = int(input("Anna joku luku: "))

if numero != 0:
    if numero % 2 == 0:
        print("Numero on parillinen")
    else: 
        print("Numero on pariton")
else: 
    print("Numero oli 0 tai negatiivinen")
