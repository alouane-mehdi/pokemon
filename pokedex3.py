import json
import os

class Pokedex:
    def __init__(self):
        self.pokemons = []
        self.charger_pokedex()

    def ajouter_pokemon(self, pokemon):
        if not any(poke['nom'] == pokemon.nom for poke in self.pokemons):
            self.pokemons.append(pokemon.to_dict())
            self.sauvegarder_pokedex()

    def sauvegarder_pokedex(self):
        with open('pokedex.json', 'w') as fichier:
            json.dump(self.pokemons, fichier, indent=4)

    def charger_pokedex(self):
        if os.path.exists('pokedex.json'):
            with open('pokedex.json', 'r') as fichier:
                self.pokemons = json.load(fichier)
        else:
            self.pokemons = []

    def obtenir_pokemons(self):
        return self.pokemons



