import json
import requests

gimme = "https://api.chucknorris.io/jokes/random"
tuli = requests.get(gimme).json()
print("\n")
print(tuli["value"])