def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

def paaohjelma():
    while True:
        gallonat = float(input("Anna bensiinin määrä gallonoina (negatiivinen luku lopettaa): "))
        if gallonat < 0:
            print("Lopetetaan ohjelma.")
            break
        litroiksi = gallonat_litroiksi(gallonat)
        print(f"{gallonat} gallonaa on {litroiksi:.2f} litraa.")

paaohjelma()
