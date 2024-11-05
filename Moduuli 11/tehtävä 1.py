class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        Julkaisu.__init__(self, nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        Julkaisu.tulosta_tiedot(self)
        print(f"Kirjailija: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumaara}")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        Julkaisu.__init__(self, nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        Julkaisu.tulosta_tiedot(self)
        print(f"Päätoimittaja: {self.paatoimittaja}")

julkaisu1 = Lehti("Aku Ankka", "Aki Hyyppä")
julkaisu2 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

julkaisu1.tulosta_tiedot()
print()
julkaisu2.tulosta_tiedot()
