import random


pisteiden_määrä = int(input("Kuinka monta pistettä arvotaan? "))


ympyran_sisällä = 0


for i in range(pisteiden_määrä):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)


    if x * 2 + y * 2 < 1:
        ympyran_sisällä += 1


pii_likiarvo = 4 * ympyran_sisällä / pisteiden_määrä


print("Piin likiarvo on:", pii_likiarvo)