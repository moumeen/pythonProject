import random


def heita_noppaa(tahkojen_maara):
    return random.randint(1, tahkojen_maara)


def paaohjelma():
    tahkojen_maara = int(input("Anna nopan tahkojen määrä: "))
    maksimi_silmaluku = int(input("Anna maksimisilmäluku, jonka haluat saavuttaa: "))

    silmaluku = 0
    while silmaluku != maksimi_silmaluku:
        silmaluku = heita_noppaa(tahkojen_maara)
        print(f"Saatu silmäluku: {silmaluku}")

    print(f"Maksimisilmäluku {maksimi_silmaluku} saavutettu!")


paaohjelma()
