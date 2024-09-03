

kaupungit = []


for i in range(5):

    kaupunki = input("Anna kaupungin nimi: ")

    kaupungit.append(kaupunki)


print("Syöttämäsi kaupungit ovat:")

for kaupunki in kaupungit:
    print(kaupunki)