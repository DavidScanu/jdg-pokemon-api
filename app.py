from pymongo import MongoClient, errors
import requests
import json
from bson.json_util import dumps
from pprint import pprint

# Connectino to Database (container: mongoDB)
try:
    client = MongoClient('mongodb://root:example@localhost:27017/')
    server_info = client.server_info()
    # print(server_info)
except errors.ServerSelectionTimeoutError as err:
    # do whatever you need
    print(err)

db = client['JDG']
collection = db['pokemons']

def populate_pokemons(collection):
    """Fonction qui rempli la collection "pokemons" avec l'api."""
    api_url = "https://pokebuildapi.fr/api/v1/pokemon"
    response = requests.get(api_url)
    pokemons = response.json()
    if isinstance(pokemons, list):
        collection.insert_many(pokemons) 

# populate_pokemons(collection)


# Ajoute pokemon 899
pokermon_899 = {"id": 899, "pokedexId": 899, "name": "Darty Papa", "image": "https://tenor.com/fr/view/kassos-darty-papa-gif-5752923", "videoYoutube": "https://www.youtube.com/watch?v=Gt5-xU1-Ows", "slug": "Darty Papa", "stats": { "HP": 100000000, "attack": 100000000, "defense": 2, "special\_attack": 100000000, "special\_defense": 2, "speed": 1 }}

def add_pokemon(collection, pokemon):
    collection.insert_one(pokemon)

# add_pokemon(collection, pokermon_899)


# Export collection
def export_collection(collection):
    docs = list(collection.find({}, {"_id": False}))
    with open("pokemons.json", "w") as file:
        json.dump(docs, file)