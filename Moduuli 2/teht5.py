leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

luotienmaara =(leiviskat * 20 * 32) + (naulat * 32) + luodit
massa = luotienmaara * 13.3

kilogramma = int(massa // 1000)
gramma = massa % 1000

print(f"\nNykyajan mittojen mukaan:")
print(f"{kilogramma} kilogrammaa ja {gramma:.2f} grammaa.")