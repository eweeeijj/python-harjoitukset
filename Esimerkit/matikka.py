import math
import random

luku1 = 3
luku2 = 4

#Yhteenlasku
print(luku1 + luku2)

#Vähennyslasku
print(luku1 - luku2)

#Kertolasku
print(luku1 * luku2)

#Desimaalijako
print(luku1 / luku2)

#Kokonaislukujako
print(luku1 // luku2)

#Jakojäännös
print(luku1 % luku2)

#Potensiin korotus
print(luku1 ** luku2)


#ESIMERKKI

pituus = float(input("Anna pituutesi: "))
paino = float(input("Anna painosi: "))

bmi = paino / (pituus / 100) **2

print("BMI:si on " , bmi)

print(f"BMI:si on {bmi:.2f}")