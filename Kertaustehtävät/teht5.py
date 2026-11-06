tarina = ""
edellinen = ""

while True:
    sana = input("Anna sana lisättäväksi tarinaan: ").strip()

    if sana.lower() == "loppu" or sana == edellinen:
        break

    if tarina == "":
        tarina = sana

    else:
        tarina = tarina + " " + sana

    edellinen = sana

    print(tarina)
    