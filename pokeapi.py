import json
import requests
ditto = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")
dittojson = ditto.json()
print(dittojson['sprites']['front_default'])