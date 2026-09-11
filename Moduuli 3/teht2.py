#LUX on parvekkeellinen hytti yläkannella
#A on ikkunallinen hytti autokannen yläpuolella
#B on ikkunaton hytti autokannen yläpuolella
#C on ikkunaton hytti autokannen alapuolella
#kelvoton hyttiluokka, ohjelma tulostaa Virheellinen hyttiluokka 

hyttiluokka = str(input("Anna hyttiluokka: "))

if hyttiluokka == "LUX":
    print("Parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print("Ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("Ikkunaton hytti autokannen alapuolella.")
elif hyttiluokka == "C":
    print("Ikkunaton hytti autokannen alapuolella.")
elif hyttiluokka not in ("LUX","A", "B","C"):
    print("Virheellinen hyttiluokka.")



