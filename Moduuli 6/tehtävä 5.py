def poista_parittomat(luku_lista):
    return [luku for luku in luku_lista if luku % 2 == 0]

def paaohjelma():
    alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    karsittu_lista = poista_parittomat(alkuperainen_lista)
    print(f"Alkuperäinen lista: {alkuperainen_lista}")
    print(f"Karsittu lista: {karsittu_lista}")

paaohjelma()
