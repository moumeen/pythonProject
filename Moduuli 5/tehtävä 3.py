#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

def on_alkuluku(luku):
    if luku <= 1:
        return False
    for jakaja in range(2, int(luku*0.5) + 1):
        if luku % jakaja == 0:
            return False
    return True


try:
    luku = int(input("Anna kokonaisluku: "))
    if on_alkuluku(luku):
        print(f"Luku {luku} on alkuluku.")
    else:
        print(f"Luku {luku} ei ole alkuluku.")
except ValueError:
    print("Syöttämäsi arvo ei ollut kelvollinen kokonaisluku.")
