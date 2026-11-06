##Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
##Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

luku = int(input("Anna luku: "))

if luku < 2:
    print("Luku ei ole alkuluku")
else:
    jaollinen = 0
    for i in range(2, luku):
        if luku % i == 0:
            jaollinen = 1
            break
    if jaollinen == 0:
        print("Luku on alkuluku")
    else:
        print("Luku ei ole alkuluku")
        
