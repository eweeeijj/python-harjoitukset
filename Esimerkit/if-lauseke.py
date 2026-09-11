raha = float(input("Kuinka paljon sinulla on rahaa? "))

if raha >= 5:
    print("Voit ostaa kahvin!")

print("Hyvää päivänjatkoa!")

# Vaikka ehto ei ole totta, se jatkaa hyvää päivänjatkoa kohtaan

# Huomioi ehto!!
# == yhtäkuin merkki, equal to  a == b
# != onko joku eri suuri kuin 
# <, >, <=, >=

pituus = int(input("Kuinka pitkä olet?"))

if 150 <= pituus <= 170: 
    print("Olet normaalipituinen!" )

# Else-haara ei voi kirjoittaa ilman if-lauseketta
# if-else rakenteessa vain ja ainoastaan yksi haara ajetaan

raha = float(input("Kuinka paljon sinulla on rahaa?"))

if raha >= 5:
    print("Voit ostaa kahvin!")
else:
    print("Sinulta puuttuu", 5-raha)

print("Hyvää päivänjatkoa!")