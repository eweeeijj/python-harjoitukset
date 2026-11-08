def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

while True:
    maara = float(input("Anna bensiinin määrä gallonoina " ))

    if maara < 0:
        print("Ohjelma lopetetaan.")
        break

    litrat = gallonat_litroiksi(maara)
    print(f"{maara} gallonaa on {litrat:.3f} litraa.\n")