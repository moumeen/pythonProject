import math
import random

# input = syötteen lukeminen
name = input ("anna nimesi:")
# name = "matti" merkkijono (string)
# \ on esape-merkki, jolla voi tuottaa esim. tabin tai rivinvaihto
print ("moi \t" + name)   # moi + matti


#age = "7"
age = input (" Anna ikäsi ")
print(" ikäsi on " + age)

age = int(age) + 1

age_string = str(age) # muutetaan int --> string, esim 8 --> "8"
print(" Ikäsi on vuoden päästä "  + age_string)
age = age + 1
# toinen tapa, tehdään tyyppimuunnos vain tarvittavan kohtaan
print(" ikäsi on kahden vuoden päästä " + str(age))

#käyttäjän pituus merkintä
height = input( "anna pituus: ")
height= float(height)
height = height + 0.1
# tulos f-strringin muodossa, ei tarvita str ()-funktiota
print(f" Nimi:{name}, Ikä: {age}, pituus: {height:.2f} metriä.")


print(math.pi)

random_number = random.randint(1, 6)
print(f"satunnainen luku 1-6:{random_number}")