def nimeet():
    nimet = set()

    while True:
        nimi = input("Syötä nimi (tai jätä tyhjäksi lopettaaksesi): ")

        if nimi == "":
            break

        if nimi in nimet:
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi")
            nimet.add(nimi)

    print("Syötetyt nimet:")
    for nimi in nimet:
        printt(nimi)



nimeet()
