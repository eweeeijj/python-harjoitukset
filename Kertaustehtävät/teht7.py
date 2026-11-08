sanat = ["kissa", "koira", "hevonen", "kana", "lammas"]
laskuri = 0

for sana in sanat:
    if len(sana) > 5:
        laskuri += 1

print(f"Listassa on {laskuri} sanaa, joissa on enemmän kuin 5 kirjainta.")
