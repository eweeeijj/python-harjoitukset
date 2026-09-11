ika = int(input("Anna ikäsi:"))

if 15 <= ika <18:
    paino = float(input("Anna painosi: "))

if ika >= 18 or ika >= 15 and paino >= 55:
    print("Lääkkeen käyttö on sallittua.")
else:
    print("Lääkkeen käyttö ei ole sallittua.")

# Monta haaraa, joilla jokaisella oma ehto
# Ohjelma jatkaa haarojen tarkistamista, kunnes se löytää lausekkeen joka on tosi (True) tai se päätyy else-haaraan

