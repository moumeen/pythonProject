# Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.
#
# LUX on parvekkeellinen hytti yläkannella.
# A on ikkunallinen hytti autokannen yläpuolella.
# B on ikkunaton hytti autokannen yläpuolella.
# C on ikkunaton hytti autokannen alapuolella.

while True:

    hyttiluokka = input("valitse hyttiluokka LUX, A, B ja C : ").upper()


    if hyttiluokka =="LUX":
        print("LUX on parvekkeellinen hytti yläkannella.")
        break
    elif hyttiluokka =="A":
        print("A on ikkunnallinen hytti autokannen yläpuoella.")
        break
    elif hyttiluokka =="B":
        print("B on ikkunaton hytti autoakannen yläpuolella")
        break
    elif hyttiluokka =="C":
        print("C on ikkunaton hytti autokannen alapuolella")
        break
    else:
        print("virheellinen hyttiluokka")



