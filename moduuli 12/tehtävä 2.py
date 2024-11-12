import requests


api_key = "7203a8738c81a193f46d59c3ae20bee3"



def hae_saatiedot(paikkakunta):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_key}&units=metric"
    vastaus = requests.get(url)

    if vastaus.status_code == 200:
        data = vastaus.json()
        kelvin_temp = data['main']['temp']
        celsius_temp = kelvin_temp
        säätila = data['weather'][0]['description']
        return säätila, celsius_temp
    else:
        print(f"Virhekoodi: {vastaus.status_code}")
        print(f"Virheilmoitus: {vastaus.text}")
        return None, None


# Pääohjelma
def main():
    paikkakunta = input("Anna paikkakunnan nimi: ")
    säätila, lämpötila = hae_saatiedot(paikkakunta)

    if säätila and lämpötila is not None:
        print(f"Säätilanne paikkakunnalla {paikkakunta}: {säätila}")
        print(f"Lämpötila: {lämpötila} °C")
    else:
        print("Tiedot eivät ole saatavilla.")


if __name__ == "__main__":
    main()
