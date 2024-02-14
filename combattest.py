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
        self.fond = pygame.image.load("assets/arenetest1.jpg")
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
        pokemon_width = 150  # Redimensionner la largeur des Pokémon pour qu'ils s'adaptent mieux à l'écran
        spacing = 20  # Espacement entre les Pokémon
        max_columns = 4  # Nombre maximum de colonnes

        total_width = pokemon_width * max_columns + spacing * (max_columns - 1)
        start_x = (self.ecran.get_width() - total_width) // 2
        start_y = 50  # Ajuster la position verticale de départ pour placer les Pokémon un peu plus haut

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for i, pokemon in enumerate(self.pokemons):
                        column = i % max_columns
                        row = i // max_columns
                        x = start_x + column * (pokemon_width + spacing)
                        y = start_y + row * (pokemon_width + spacing)
                        pokemon_rect = pygame.Rect(x, y, pokemon_width, pokemon_width)
                        if pokemon_rect.collidepoint(pos):
                            return pokemon

            self.ecran.blit(self.fond, (0, 0))
            self.afficher_tous_les_pokemon(start_x, start_y, pokemon_width, spacing, max_columns)
            pygame.display.flip()

    def afficher_tous_les_pokemon(self, start_x, start_y, pokemon_width, spacing, max_columns):
        max_rows = (len(self.pokemons) + max_columns - 1) // max_columns

        for i, pokemon in enumerate(self.pokemons):
            column = i % max_columns
            row = i // max_columns
            x = start_x + column * (pokemon_width + spacing)
            y = start_y + row * (pokemon_width + spacing)

            # Redimensionner l'image du Pokémon pour qu'elle s'adapte au cadre
            pokemon_image = pygame.transform.scale(pokemon.image, (pokemon_width, pokemon_width))

            # Afficher l'image du Pokémon
            self.ecran.blit(pokemon_image, (x, y))

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

                    # Déplacer les Pokémon combattants vers le bas de l'écran
                    start_y = 400  # Nouvelle position Y pour les Pokémon combattants
                    self.afficher_tous_les_pokemon(0, start_y, 150, 20, 4)

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

