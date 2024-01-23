"""
This script imports the requests library and calls an existing
Chuck Norris API to get a random joke. It's jokes are explicit,
so use caution. I was disappointed with the lewdness if I'm being
honest. 

But its a decent example of an http request to an open api.
"""
import requests  # http request lib
from rich import print  # prints to the terminal better

r = requests.get("https://api.chucknorris.io/jokes/random")

print(r.json())

data = r.json()

print(f"Chuck says:{data['value']}")