
import pygame

class Pokemon:
    def __init__(self, nom, type_pokemon, description, image):
        self.nom = nom
        self.type = type_pokemon
        self.description = description
        self.image = image

    def afficher_info(self, afficher_details):
        if afficher_details:
            return f"Type: {self.type}, Description: {self.description}"
        else:
            return ""

class Pokedex:
    def __init__(self):
        self.pokemons = []

    def ajouter_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

def afficher_pokedex_pygame(pokedex, fond_ecran, chemin_musique):
    pygame.init()
    pygame.mixer.init()  # Initialise le mixer

    # Définir la taille de la fenêtre
    width, height = 1200, 700
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pokedex")

    # Charger l'image de fond
    fond = pygame.image.load(fond_ecran)
    fond = pygame.transform.scale(fond, (width, height))

    # Charger et jouer la musique de fond
    pygame.mixer.music.load(chemin_musique)
    pygame.mixer.music.play(-1)

    # Charger les images des Pokémon
    images = {}
    rect_images = {}
    for pokemon in pokedex.pokemons:
        try:
            images[pokemon.nom] = pygame.image.load(pokemon.image)
            rect_images[pokemon.nom] = images[pokemon.nom].get_rect()
        except pygame.error:
            print(f"Erreur lors du chargement de l'image pour {pokemon.nom}")
            images[pokemon.nom] = None

    afficher_details = {pokemon.nom: False for pokemon in pokedex.pokemons}
    running = True
    while running:
        screen.blit(fond, (0, 0))  # Dessiner l'image de fond

        y = 20
        for pokemon in pokedex.pokemons:
            font = pygame.font.SysFont(None, 36)

            # Positionnement des Pokémon
            if pokemon.nom in ["Pikachu", "Salameche"]:
                position_x = width - 150
                details_x = 20  # Description à gauche pour les Pokémon à droite
            else:
                position_x = 20
                details_x = (width // 2) - 200  # Description plus centrée pour Bulbizarre et Carapuce

            nom_text = font.render(pokemon.nom, True, (0, 0, 0))
            screen.blit(nom_text, (position_x, y))

            if images[pokemon.nom]:
                img = pygame.transform.scale(images[pokemon.nom], (100, 100))
                img_rect = img.get_rect(topleft=(position_x, y + 40))
                rect_images[pokemon.nom] = img_rect
                screen.blit(img, img_rect)

            if afficher_details[pokemon.nom]:
                details_text = font.render(pokemon.afficher_info(True), True, (0, 0, 0))
                screen.blit(details_text, (details_x, y))

            y += 160
            if y > height:
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for pokemon in pokedex.pokemons:
                    if rect_images[pokemon.nom].collidepoint(event.pos):
                        afficher_details[pokemon.nom] = not afficher_details[pokemon.nom]

        pygame.display.flip()

    pygame.mixer.music.stop()
    pygame.quit()

# Création de 4 Pokémons avec des images
pikachu = Pokemon("Pikachu", "Électrique", "Célèbre pour ses joues électriques.", "image/pikachu.png")
bulbizarre = Pokemon("Bulbizarre", "Plante/Poison", "Possède une plante sur son dos.", "image/Bulbizarre.png")
salamèche = Pokemon("Salameche", "Feu", "Sa queue est enflammée quand il est en bonne santé.", "image/salameche.png")
carapuce = Pokemon("Carapuce", "Eau", "Un petit Pokémon tortue.", "image/carapuce.png")

# Création du Pokedex et ajout des Pokémons
mon_pokedex = Pokedex()
mon_pokedex.ajouter_pokemon(pikachu)
mon_pokedex.ajouter_pokemon(bulbizarre)
mon_pokedex.ajouter_pokemon(salamèche)
mon_pokedex.ajouter_pokemon(carapuce)

# Chemin vers l'image de fond et la musique
fond_ecran = "image/fond-ecran2.jpg"
chemin_musique = "music/Tetris2.mp3"  

# Affichage du Pokedex avec Pygame
afficher_pokedex_pygame(mon_pokedex, fond_ecran, chemin_musique)