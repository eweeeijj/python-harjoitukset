pituus = int(input("Anna kuhan pituus: "))
mitta = 37

if pituus < mitta:
    puuttuu = mitta-pituus
    print ("Laske kuha järveen, se on alimittainen", puuttuu, "cm")
else:
    print("Kuhan saa nostaa!")