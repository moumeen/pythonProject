class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.matkamittari = 0

    def aja(self, tuntia):
        self.matkamittari += self.huippunopeus * tuntia

    def tulosta_tiedot(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus} km/h")
        print(f"Matkamittarilukema: {self.matkamittari} km")


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        Auto.__init__(self, rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def tulosta_tiedot(self):
        Auto.tulosta_tiedot(self)
        print(f"Akkukapasiteetti: {self.akkukapasiteetti} kWh")


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        Auto.__init__(self, rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

    def tulosta_tiedot(self):
        Auto.tulosta_tiedot(self)
        print(f"Bensatankin koko: {self.bensatankin_koko} l")


sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.aja(3)
polttomoottoriauto.aja(3)

print("Sähköauto:")
sahkoauto.tulosta_tiedot()
print()
print("Polttomoottoriauto:")
polttomoottoriauto.tulosta_tiedot()
