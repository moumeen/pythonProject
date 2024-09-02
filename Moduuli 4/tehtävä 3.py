#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.


luvut = []

while True:
    syöte = input("Syötä luku (tyhjällä merkkijonolla lopetetaan): ")

    if syöte == "":
        break

    try:
        luku = int(syöte)
        luvut.append(luku)
    except ValueError:
        print("Virheellinen syöte, yritä uudelleen.")


if luvut:
    pienin = min(luvut)
    suurin = max(luvut)

    print(f"Pienin luku on: {pienin}")
    print(f"Suurin luku on: {suurin}")
else:
    print("Ei syötettyjä lukuja.")
