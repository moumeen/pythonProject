#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

import random


lukumaara = int(input("anna arpakuutioiden lukumäärä: "))

silmalukujen_summa = 0

for i in range(lukumaara):
    silmäluku = random.randint(1,6)
    silmalukujen_summa += silmäluku

print(f"Kaikkien silmälukujenlukujen summa on {silmalukujen_summa}")
