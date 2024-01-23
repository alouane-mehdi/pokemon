import pygame
import json
import os

class Pokemon:
    def __init__(self, nom, type_pokemon, defense, puissance, pv, description, image):
        self.nom = nom
        self.type = type_pokemon
        self.defense = defense
        self.puissance = puissance
        self.pv = pv
        self.description = description
        self.image = image

    def to_dict(self):
        return {
            "nom": self.nom,
            "type": self.type,
            "defense": self.defense,
            "puissance": self.puissance,
            "pv": self.pv,
            "description": self.description,
            "image": self.image
        }

class Pokedex:
    def __init__(self):
        self.pokemons = []
        self.charger_pokedex()

    def ajouter_pokemon(self, pokemon):
        if not any(poke["nom"] == pokemon.nom for poke in self.pokemons):
            self.pokemons.append(pokemon.to_dict())
            self.sauvegarder_pokedex()

    def sauvegarder_pokedex(self):
        with open('pokedex.json', 'w') as fichier:
            json.dump(self.pokemons, fichier, indent=4)

    def charger_pokedex(self):
        if os.path.exists('pokedex.json'):
            with open('pokedex.json', 'r') as fichier:
                self.pokemons = json.load(fichier)

def afficher_pokedex_pygame(pokedex, fond_ecran, chemin_musique):
    pygame.init()
    pygame.mixer.init()
    width, height = 950, 700
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pokedex")
    fond = pygame.image.load(fond_ecran)
    fond = pygame.transform.scale(fond, (width, height))
    pygame.mixer.music.load(chemin_musique)
    pygame.mixer.music.play(-1)
    images = {}
    rect_images = {}
    for pokemon in pokedex.pokemons:
        try:
            images[pokemon["nom"]] = pygame.image.load(pokemon["image"])
            rect_images[pokemon["nom"]] = images[pokemon["nom"]].get_rect()
        except pygame.error:
            print(f"Erreur lors du chargement de l'image pour {pokemon['nom']}")
            images[pokemon["nom"]] = None
    running = True
    while running:
        screen.blit(fond, (0, 0))
        y = 20
        for pokemon in pokedex.pokemons:
            font = pygame.font.SysFont(None, 30)
            nom_text = font.render(pokemon["nom"], True, (0, 0, 0))
            screen.blit(nom_text, (20, y))
            if images[pokemon["nom"]]:
                img = pygame.transform.scale(images[pokemon["nom"]], (100, 100))
                img_rect = img.get_rect(topleft=(20, y + 40))
                rect_images[pokemon["nom"]] = img_rect
                screen.blit(img, img_rect)
            y += 160
            if y > height:
                break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    
    pygame.mixer.music.stop()
    pygame.quit()

    # Création du Pokedex et ajout des Pokémons
mon_pokedex = Pokedex()

# Assurez-vous que les chemins des images et des fichiers sont corrects.
pikachu = Pokemon("Pikachu", "Électrique", 35, 55, 40, "Célèbre pour ses joues électriques.", "image/pikachu.png")
bulbizarre = Pokemon("Bulbizarre", "Plante/Poison", 30, 45, 35, "Possède une plante sur son dos.", "image/bulbizarre.png")
salamèche = Pokemon("Salameche", "Feu", 25, 60, 39, "Sa queue est enflammée quand il est en bonne santé.", "image/salameche.png")
carapuce = Pokemon("Carapuce", "Eau", 40, 50, 44, "Un petit Pokémon tortue.", "image/carapuce.png")

mon_pokedex.ajouter_pokemon(pikachu)
mon_pokedex.ajouter_pokemon(bulbizarre)
mon_pokedex.ajouter_pokemon(salamèche)
mon_pokedex.ajouter_pokemon(carapuce)

# Chemin vers l'image de fond et la musique
fond_ecran = "image/fond-ecran.png"
chemin_musique = "music/Tetris.mp3"

# Affichage du Pokedex avec Pygame
pokemon_affichage = afficher_pokedex_pygame(mon_pokedex, fond_ecran, chemin_musique)

