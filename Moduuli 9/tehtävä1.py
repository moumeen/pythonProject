# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin. Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.


import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinennopeus = 0
        self.kuljettumatka = 0

    def printtaa_tiedot(self):
        print(
            f"Rekisteritunnus: {self.rekisteritunnus}, "
            f"Huippunopeus: {self.huippunopeus} km/h, "
            f"Tämänhetkinen nopeus: {self.tamanhetkinennopeus} km/h, "
            f"Kuljettu matka: {self.kuljettumatka} km."
        )

    def kiihdyta(self, muutos):
        uusi_nopeus = self.tamanhetkinennopeus + muutos
        if uusi_nopeus > self.huippunopeus:
            self.tamanhetkinennopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tamanhetkinennopeus = 0
        else:
            self.tamanhetkinennopeus = uusi_nopeus

    def kulje(self, tunnit):
        matka = self.tamanhetkinennopeus * tunnit
        self.kuljettumatka += matka


# Pääohjelma
auto_lista = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    auto_lista.append(Auto(rekisteritunnus, huippunopeus))

kilpailu_paattynyt = False

while not kilpailu_paattynyt:
    for auto in auto_lista:
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)
        auto.kulje(1)  # Liikkuminen yhden tunnin ajan

        if auto.kuljettumatka >= 10000:
            kilpailu_paattynyt = True
            break

print("\nKilpailun tulokset:")
print( f"{'Rekisteritunnus':<10} {'Huippunopeus (km/h)':<20} {'Tämänhetkinen nopeus (km/h)':<25} {'Kuljettu matka (km)':<15}")
for auto in auto_lista:
    auto.printtaa_tiedot()