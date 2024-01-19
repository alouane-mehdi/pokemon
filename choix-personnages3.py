import pygame
import sys
from pokemon3 import Pokemon
from combat3 import Combat

def choisir_pokemon(pokemons, ecran, fond):
    pokemon_width = 200
    spacing = 50
    total_width = pokemon_width * len(pokemons) + spacing * (len(pokemons) - 1)
    start_x = (ecran.get_width() - total_width) // 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for i, pokemon in enumerate(pokemons):
                    if pygame.Rect(start_x + i * (pokemon_width + spacing), 50, pokemon_width, 200).collidepoint(pos):
                        return pokemon

        ecran.blit(fond, (0, 0))
        for i, pokemon in enumerate(pokemons):
            ecran.blit(pokemon.image, (start_x + i * (pokemon_width + spacing), 50))
        pygame.display.flip()

# Initialisation de Pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("music/street-fight.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Création des Pokémon
pikachu = Pokemon("Pikachu", "Électrique", 30, "Célèbre pour ses joues électriques.", "image/pikachu.png")
bulbizarre = Pokemon("Bulbizarre", "Plante/Poison", 35, "Possède une plante sur son dos.", "image/bulbizarre.png")
salameche = Pokemon("Salameche", "Feu", 33, "Sa queue est enflammée quand il est en bonne santé.", "image/salameche.png")
carapuce = Pokemon("Carapuce", "Eau", 32, "Un petit Pokémon tortue.", "image/carapuce.png")

# Création de la fenêtre principale
ecran = pygame.display.set_mode((950, 400))
pygame.display.set_caption("Pokémon Combat Simulator")
fond = pygame.image.load("image/arene.webp")
fond = pygame.transform.scale(fond, (950, 400))

pokemons = [pikachu, bulbizarre, salameche, carapuce]

# Boucle principale du jeu
while True:
    pokemon_joueur = choisir_pokemon(pokemons, ecran, fond)
    ennemis_potentiels = [p for p in pokemons if p != pokemon_joueur]
    combat = Combat(pokemon_joueur, ennemis_potentiels, ecran, fond)
    fin_combat = combat.lancer_combat()

    # Réinitialisez la vie des Pokémon après le combat
    pokemon_joueur.reinitialiser_vie()
    for ennemi in ennemis_potentiels:
        ennemi.reinitialiser_vie()

    if not fin_combat:
        break  # Sortie de la boucle si le jeu est quitté

pygame.quit()

