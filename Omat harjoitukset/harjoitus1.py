#HARJOITUS 1
nimi = input("Anna nimesi: ")
print("Hei, " + nimi + "!")

#HARJOITUS 2
import math
sade = float(input("Anna ympyrän säde: "))
pintaala = math.pi * sade ** 2

print("Ympyrän pinta-ala on: ", pintaala)


#HARJOITUS 3
import math
kanta = float(input("Anna ympyrän kanta: "))
korkeus = float(input("Anna ympyrän korkeus: "))
pintaala = kanta * korkeus

print("Suorakulmion pinta-ala on: ", pintaala)

#HARJOITUS 4
luku1 = int(input("Anna kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))
luku3 = int(input("Anna kolmas kokonaisluku: "))

summa = (luku1 + luku2 + luku3)
tulo = (luku1 * luku2 * luku3)
keskiarvo = (luku1 + luku2 + luku3) // 3

print("Lukujen summa on: ", summa)
print("Lukujen tulo on: ", tulo)
print("Lukujen keskiarvo on: ", keskiarvo)

#HARJOITUS 5
leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

luoti_grammoina = 13.3
naula_grammoina = 32 * luoti_grammoina
leiviska_grammoina = 20 * naula_grammoina 

massa_grammoina = (leiviskat * leiviska_grammoina) + (naulat * naula_grammoina) + (luodit * luoti_grammoina)

print(f"\nNykyajan mittojen mukaan: ")
kilot = massa_grammoina // 1000
grammat = massa_grammoina % 1000

print(f"{kilot} kilogrammaa ja {grammat:.2f} grammaa.")


