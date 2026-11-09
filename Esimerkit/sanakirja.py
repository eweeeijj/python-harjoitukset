puhelinluettelo = {"Viivi" : "050-1234567",
                   "Ahmed" : "040-1112223",
                   "Pekka" : "050-7654321"}

print(puhelinluettelo)

# Alkion arvon muuttaminen
puhelinluettelo ["Pekka"] = "045-1234567"

print(puhelinluettelo)

# Alkion lisääminen
puhelinluettelo["Olga"] = "050-2345678"
print(puhelinluettelo)

# Arvon poistaminen
del puhelinluettelo["Viivi"]
print(puhelinluettelo)

# Sanakirjassa on aaltosulkeet!
# Sanakirjan voi kirjoittaa myös putkeen, tai erotella riveille! 

# Tulostaa avaimet
for numero in puhelinluettelo:
    print(numero)

# Tulostaa arvot
for numero in puhelinluettelo.values():
    print(numero)

# Tulostaa molemmat / käytetään koko alkiota
for avain, numero in puhelinluettelo.items():
    print(f"{avain}n puhelinnumero on {numero}")



koordinaatit = {"helsinki" : (67, 31),
                 "Vantaa" : (81, 55),
                  "Espoo" : (27, 68) 
                }

# Alkio voi sisältää tietorakenteen
    