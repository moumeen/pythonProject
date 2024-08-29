#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi. Vuosi on karkausvuosi, jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.


vuosiluku = int(input("Vuosiluku: "))

if (vuosiluku % 400 == 0):
    print(f"{vuosiluku} on karkausvuosi.")
elif (vuosiluku % 100 == 0):
    print(f"{vuosiluku} ei ole karkausvuosi.")
elif (vuosiluku % 4 == 0):
    print(f"{vuosiluku} on karkausvuosi.")
else:
    print(f"{vuosiluku} ei ole karkausvuosi.")




