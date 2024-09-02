
oikea_kayttajatunnus = "python"
oikea_salasana = "rules"


max_yritykset = 5


yritysten_maara = 0


while yritysten_maara < max_yritykset:

    kayttajatunnus = input("Syötä käyttäjätunnus: ")
    salasana = input("Syötä salasana: ")


    if kayttajatunnus == oikea_kayttajatunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break
    else:
        yritysten_maara += 1

        if yritysten_maara < max_yritykset:
            print(f"Tunnus tai salasana on väärin. Yritä uudelleen. (Yrityksiä jäljellä: {max_yritykset - yritysten_maara})")
        else:
            print("ohjelma sulkeutuu.")
