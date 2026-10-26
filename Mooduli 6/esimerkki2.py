def vaihda():
    kaupunki = "Vantaa" 
    print("Funktiossa lopuksi: " + kaupunki)
    return

#PÄÄOHJELMA
kaupunki = "Helsinki" 
print("Glopbaalin kaupungin nimi alunperin: " + kaupunki)
vaihda()
print("Globaalin kaupungin nimi: " + kaupunki)


#Globaalia muuttujaa voi käyttää funktiossa, mutta paikallista (funktion sisällä olevaa)
# muuttujaa ei voi käyttää pääohjelmassa. 
