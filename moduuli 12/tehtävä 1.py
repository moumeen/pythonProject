import requests

def hae_chuck_norris_vitsi():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        vastaus = requests.get(url)
        if vastaus.status_code == 200:
            data = vastaus.json()
            print(data["value"])
        else:
            print("Virhe säätiedon hakemisessa.")
    except Exception as e:
        print(f"Virhe: {e}")

hae_chuck_norris_vitsi()
