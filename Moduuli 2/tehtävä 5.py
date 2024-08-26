

leiviskät = float(input("Anna leiviskät: "))
naulat = float(input("anna naulat: "))
luodit = float(input("anna luodit: "))

#ensin selvitetään kuinka paljon meillä on nauloja

naulatiito = leiviskät * 20 + naulat

# sitten selvitellään kuinka paljon meillä on luoteja yhteensä
luoditiito = naulatiito * 32 + luodit



# nyt kun tiedämme määrän niin lasketaan massa ensin grammoina
grammatTot = luoditiito * 13.3
print(grammatTot)

kg = int(grammatTot // 1000)
gr = grammatTot % 1000
print(f"Massa nykymittojen mukaan: {kg} kg ja {gr:.2f} grammaa")




