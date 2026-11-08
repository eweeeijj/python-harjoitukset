import math

def laske_yksikkohinta(halkaisija_cm, hinta_euro):
    sade_m = (halkaisija_cm / 2) / 100
    pinta_ala_m2 = math.pi * (sade_m ** 2)
    return hinta_euro / pinta_ala_m2

halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta: "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija: "))
hinta2 = float(input("Anna toisen pizzan hinta: "))

yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

print(f"\nEnsimmäisen pizzan yksikköhinta: {yksikkohinta1:.2f} €/m2")
print(f"\nToisen pizzan yksikköhinta: {yksikkohinta2:.2f} €/m2")

if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle. ")
elif yksikkohinta2 < yksikkohinta1:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Molemmat pizzat antavat yhtä hyvän vastineen rahalle.")