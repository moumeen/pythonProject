#Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

n = 1

while n <= 1000:
    if n % 3 == 0:
        print(n)
    n = n + 1

