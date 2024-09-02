#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm




while True:
    tuumat = float(input("anna tuuma (negatiivinen numero lopettaa) : "))

    if tuumat < 0:
        print("ohjelma päättyy")
        break
    else:
        senttimetri = tuumat * 2.54
        print(f"{tuumat} tuumaa on {senttimetri} senttimetriä")





