def koordinaatti(_x, _y):
    piste = (_x, _y)
    return piste

x = int(input("Anna x koordinaatti: "))
y = int(input("Anna y koordinaatti: "))

karttapiste = koordinaatti(x, y)
print("Kohde kartalla on koordinaatissa:", karttapiste)
