kustannukset = [12.5, 8.2, 15.0, 6.5, 10.8]
yhteensa = 0.0

for  hinta in kustannukset: 
    print(f"Tuotteen valmistuskustannus: {hinta} €")
    yhteensa += hinta

print(f"Valmistuskustannukset yhteensä: {yhteensa} €")