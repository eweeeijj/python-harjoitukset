# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l
# Ohjelma kysyy sukupuolen ja hemoglobiiniarvon
# Ilmoittaa, onko hemoglobiini alhainen, normaali vai korkea

sukupuoli = str(input("Anna sukupuolesi: "))
hemoglobiini = int(input("Anna hemoglobiiniarvosi: "))

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemoglobiini >= 117 and hemoglobiini <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    elif hemoglobiini >175: 
        print ("Hemoglobiiniarvosi on korkea.")
if sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemoglobiini >= 134 and hemoglobiini <=195:
        print("Hemoglobiiniarvosi on normaali.")
    elif hemoglobiini >195:
        print("Hemoglobiiniarvosi on korkea.")
