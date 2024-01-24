import pygame
import sys
from pokedex3 import Pokedex
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

def afficher_pokedex(ecran, pokedex):
    font = pygame.font.SysFont(None, 36)
    ecran.fill((255, 255, 255))  # Remplit l'écran avec une couleur blanche

    for i, pokemon in enumerate(pokedex.obtenir_pokemons()):
        nom_text = font.render(pokemon["nom"], True, (0, 0, 0))
        ecran.blit(nom_text, (20, 30 + i * 40))

        try:
            image = pygame.image.load(pokemon["chemin_image"])
            image = pygame.transform.scale(image, (100, 100))
            ecran.blit(image, (200, 20 + i * 40))
        except pygame.error:
            print(f"Erreur lors du chargement de l'image pour {pokemon['nom']}")

# Initialisation de Pygame et chargement des ressources
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("music/street-fight.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

mon_pokedex = Pokedex()

ecran = pygame.display.set_mode((950, 400))
pygame.display.set_caption("Pokémon Combat Simulator")
fond = pygame.image.load("image/arene.webp")
fond = pygame.transform.scale(fond, (950, 400))

# Création des Pokémon
pikachu = Pokemon("Pikachu", "Électrique", 30, "Célèbre pour ses joues électriques.", "image/pikachu.png")
bulbizarre = Pokemon("Bulbizarre", "Plante/Poison", 35, "Possède une plante sur son dos.", "image/bulbizarre.png")
salameche = Pokemon("Salameche", "Feu", 33, "Sa queue est enflammée quand il est en bonne santé.", "image/salameche.png")
carapuce = Pokemon("Carapuce", "Eau", 32, "Un petit Pokémon tortue.", "image/carapuce.png")

pokemons = [pikachu, bulbizarre, salameche, carapuce]
pokemons_combattus = []  # Pour garder une trace des Pokémon combattus
afficher_pokedex_flag = False

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                afficher_pokedex_flag = not afficher_pokedex_flag

    if afficher_pokedex_flag:
        afficher_pokedex(ecran, mon_pokedex)
    else:
        pokemon_joueur = choisir_pokemon(pokemons, ecran, fond)
        if pokemon_joueur:
            pokemons_combattus.append(pokemon_joueur)  # Ajout du Pokémon choisi à la liste des combattus

            ennemis_potentiels = [p for p in pokemons if p != pokemon_joueur]
            combat = Combat(pokemon_joueur, ennemis_potentiels, ecran, fond)
            fin_combat = combat.lancer_combat()

            for ennemi in ennemis_potentiels:
                pokemons_combattus.append(ennemi)  # Ajout des ennemis combattus à la liste

            pokemon_joueur.reinitialiser_vie()
            for ennemi in ennemis_potentiels:
                ennemi.reinitialiser_vie()

            if not fin_combat:
                break

    # Enregistrement uniquement des Pokémon combattus dans le Pokédex
    for pokemon in pokemons_combattus:
        if not any(p['nom'] == pokemon.nom for p in mon_pokedex.obtenir_pokemons()):
            mon_pokedex.ajouter_pokemon(pokemon)

    pokemons_combattus.clear()  # Réinitialisation de la liste après l'enregistrement

    pygame.display.flip()

pygame.quit()









