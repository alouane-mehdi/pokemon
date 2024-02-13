import pygame
import sys
import json
from pokedex3 import Pokedex
from pokemon3 import Pokemon
from combat3 import Combat

class PokemonGame:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("music/street-fight.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        self.mon_pokedex = Pokedex()
        self.ecran = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Pokémon Combat Simulator")
        self.fond = pygame.image.load("image/arene.webp")
        self.fond = pygame.transform.scale(self.fond, (1280, 720))
        self.pokemons_combattus = []
        self.afficher_pokedex_flag = False
        self.pokemon_vaincu = None

        # Charger les données des Pokémon depuis le fichier JSON
        with open('pokedex.json', 'r') as fichier:
            pokemons_data = json.load(fichier)
        
        # Créer les objets Pokémon à partir des données chargées depuis le JSON
        self.pokemons = []
        for pokemon_data in pokemons_data:
            pokemon = Pokemon(pokemon_data["nom"], pokemon_data["type_pokemon"], pokemon_data["vie_max"], pokemon_data["description"], pokemon_data["chemin_image"])
            self.pokemons.append(pokemon)

    def choisir_pokemon(self):
        pokemon_width = 200
        spacing = 50
        total_width = pokemon_width * len(self.pokemons) + spacing * (len(self.pokemons) - 1)
        start_x = (self.ecran.get_width() - total_width) // 2

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for i, pokemon in enumerate(self.pokemons):
                        if pygame.Rect(start_x + i * (pokemon_width + spacing), 50, pokemon_width, 200).collidepoint(pos):
                            return pokemon

            self.ecran.blit(self.fond, (0, 0))
            for i, pokemon in enumerate(self.pokemons):
                self.ecran.blit(pokemon.image, (start_x + i * (pokemon_width + spacing), 50))
            pygame.display.flip()

    def afficher_pokedex(self):
        font = pygame.font.SysFont(None, 36)
        fond_pokedex = pygame.image.load("image/pokemon-theme2.png")
        self.ecran.blit(fond_pokedex, (0, 0))

        if self.pokemon_vaincu:
            pokemon = next((p for p in self.mon_pokedex.obtenir_pokemons() if p["nom"] == self.pokemon_vaincu["nom"]), None)
            if pokemon:
                nom_text = font.render(pokemon["nom"], True, (0, 0, 0))
                self.ecran.blit(nom_text, (20, 30))
                
                try:
                    image = pygame.image.load(pokemon["chemin_image"])
                    image = pygame.transform.scale(image, (100, 100))
                    self.ecran.blit(image, (200, 20))
                except pygame.error:
                    print(f"Erreur lors du chargement de l'image pour {pokemon['nom']}")
                pygame.display.flip()  # Actualiser l'affichage après avoir ajouté le texte et l'image

    def afficher_tous_les_pokemon(self):
        pokemon_width = 200
        pokemon_height = 200
        spacing = 50
        max_columns = 4  # Nombre maximum de colonnes

        # Calcul du nombre de lignes nécessaires en fonction du nombre total de Pokémon
        total_pokemon = len(self.pokemons)
        max_rows = (total_pokemon + max_columns - 1) // max_columns

        cell_width = (self.ecran.get_width() - (max_columns + 1) * spacing) // max_columns
        cell_height = (self.ecran.get_height() - (max_rows + 1) * spacing) // max_rows

        for i, pokemon in enumerate(self.pokemons):
            row = i // max_columns
            column = i % max_columns
            x = spacing + column * (cell_width + spacing)
            y = spacing + row * (cell_height + spacing)

            pokemon_image = pygame.transform.scale(pokemon.image, (cell_width, cell_height))
            self.ecran.blit(pokemon_image, (x, y))

        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.afficher_pokedex_flag = not self.afficher_pokedex_flag

            if self.afficher_pokedex_flag:
                self.afficher_pokedex()
            else:
                pokemon_joueur = self.choisir_pokemon()
                if pokemon_joueur:
                    self.pokemons_combattus.append(pokemon_joueur)

                    ennemis_potentiels = [p for p in self.pokemons if p != pokemon_joueur]
                    combat = Combat(pokemon_joueur, ennemis_potentiels, self.ecran, self.fond)
                    fin_combat = combat.lancer_combat()

                    for ennemi in ennemis_potentiels:
                        self.pokemons_combattus.append(ennemi)

                    pokemon_joueur.reinitialiser_vie()
                    for ennemi in ennemis_potentiels:
                        ennemi.reinitialiser_vie()

                    if not fin_combat:
                        self.pokemon_vaincu = pokemon_joueur.to_dict()

            pygame.display.flip()

if __name__ == "__main__":
    game = PokemonGame()
    game.run()







