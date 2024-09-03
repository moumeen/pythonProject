#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.


numerot = []
while True:
    numero = input("anna luku: ")

    if numero == "":
        break

    try:

        numero = int(numero)
        numerot.append(numero)
    except ValueError:

        print("Syöttämäsi arvo ei ollut kelvollinen luku. Yritä uudelleen.")


numerot.sort(reverse=True)

print("Syöttämäsi luvut ovat:", numerot[:5])









