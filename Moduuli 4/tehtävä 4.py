#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random
salainen_numero = random.randint(1, 10)

print("Arvaa luku väliltä 1-10.")

while True:
    try:
        luku = int(input("Anna luku: "))

        if luku < 1 or luku > 10:
            print("Syötetty luku on väliltä 1-10. Yritä uudelleen.")
        elif luku < salainen_numero:
            print("Luku on pienempi kuin arvottu luku.")
        elif luku > salainen_numero:
            print("Luku on suurempi kuin arvottu luku.")
        else:
            print("Oikein! Voitit pelin!")
            break
    except ValueError:
        print("Virheellinen syöte. Syötä vain kokonaisluku.")