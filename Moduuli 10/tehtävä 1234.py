

#tehtävä 1

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        while self.nykyinen_kerros < kohde_kerros:
             self.kerros_ylös()
        while self.nykyinen_kerros > kohde_kerros:
             self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")


h = Hissi(1, 10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)


# tehtävä 2

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_maara)]

    def aja_hissiä(self, hissi_numero, kohde_kerros):
        if 0 <= hissi_numero < len(self.hissit):
            print(f"Ajetaan hissiä {hissi_numero} kerrokseen {kohde_kerros}")
            self.hissit[hissi_numero].siirry_kerrokseen(kohde_kerros)


talo = Talo(1, 10, 3)
talo.aja_hissiä(0, 5)
talo.aja_hissiä(1, 8)
talo.aja_hissiä(2, 3)


# tehtävä 3

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_maara)]

    def aja_hissiä(self, hissi_numero, kohde_kerros):
        if 0 <= hissi_numero < len(self.hissit):
            print(f"Ajetaan hissiä {hissi_numero} kerrokseen {kohde_kerros}")
            self.hissit[hissi_numero].siirry_kerrokseen(kohde_kerros)

    def palohälytys(self):
        print("Palohälytys! Kaikki hissit siirretään pohjakerrokseen.")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.hissit[0].alin_kerros)


talo = Talo(1, 10, 3)
talo.aja_hissiä(0, 5)
talo.aja_hissiä(1, 8)
talo.palohälytys()


# tehtävä 4
import random

class Auto:
    def __init__(self, nimi, huippunopeus):
        self.nimi = nimi
        self.huippunopeus = huippunopeus
        self.matka = 0
        self.nopeus = 0

    def kulje(self, tunti):
        self.matka += self.nopeus * tunti

class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.nopeus = max(0, min(auto.huippunopeus, auto.nopeus + muutos))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\nTilanne kilpailussa '{self.nimi}':")
        print(f"{'Auto':<10}{'Matka (km)':<10}{'Nopeus (km/h)':<15}")
        for auto in self.autot:
            print(f"{auto.nimi:<10}{auto.matka:<10}{auto.nopeus:<15}")

    def kilpailu_ohi(self):
        return any(auto.matka >= self.pituus_km for auto in self.autot)


autot = [Auto(f"Auto {i+1}", random.randint(100, 200)) for i in range(10)]
kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()

kilpailu.tulosta_tilanne()
print("Kilpailu on päättynyt!")
