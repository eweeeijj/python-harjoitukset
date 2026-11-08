#MÄÄRITELLÄÄN FUNKTIO ENNEN KUIN SITÄ VOI KUTSUA 

def tervehdi(tervehdys, kerrat):
    for i in range(kerrat):
        print("tervehdys " + str(i+1) + ".kerran.")
        return
    

#PÄÄOHJHELMA

print("Testataan tervehdys-funktiota:")
tervehdi("Tervehdys", 3)
print("Testataan vielä varmistukseksi..")
tervehdi("Moi", 5)



#FUNKTIO TÄYTYY MÄÄRITELLÄ, ENNEN KUIN SITÄ VOI KUTSUA, ETTÄ SITÄ VOI KÄYTTÄÄ!! copikjk