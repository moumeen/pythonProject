def pää():
    vuodenajat = (
        "talvi",
        "kevät",
        "kesä",
        "syksy"
    )

    kuukausi = int(input("Anna kuukauden numero (1-12): "))

    if 1 <= kuukausi <= 12:
        vuodenajan_indeksi = (kuukausi - 1) // 3
        print(f"{kuukausi}. kuukauden vuoden aika on {vuodenajat[vuodenajan_indeksi]}.")
    else:
        print("Virheellinen kuukausinumero. Anna numero välillä 1-12.")

pää()
