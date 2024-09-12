def kyllä():
    lentoasemat = {}

    while True:
        print("Valitse toiminto:")
        print("1. Syötä uusi lentoasema")
        print("2. Hae lentoaseman tiedot")
        print("3. Lopeta")

        valinta = input("Syötä valinta (1/2/3): ")

        if valinta == "1":
            icao_koodi = input("Syötä lentoaseman ICAO-koodi: ")
            nimi = input("Syötä lentoaseman nimi: ")
            lentoasemat[icao_koodi] = nimi
            print(f"Lentoasema '{nimi}' lisätty ICAO-koodilla '{icao_koodi}'.")

        elif valinta == "2":
            icao_koodi = input("Syötä lentoaseman ICAO-koodi: ")
            if icao_koodi in lentoasemat:
                print(f"Lentoaseman nimi ICAO-koodilla '{icao_koodi}' on {lentoasemat[icao_koodi]}.")
            else:
                print("Lentoasemaa ei löydy.")

        elif valinta == "3":
            print("Ohjelma lopetetaan.")
            break

        else:
            print("Virheellinen valinta. Yritä uudelleen.")


kyllä()
