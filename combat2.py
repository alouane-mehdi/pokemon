import pygame
import sys
import random

# Définition de la classe Pokemon
class Pokemon:
    def __init__(self, nom, type_pokemon, vie, description, chemin_image):
        self.nom = nom
        self.type = type_pokemon
        self.vie = vie
        self.description = description
        self.image = pygame.image.load(chemin_image)
        self.image = pygame.transform.scale(self.image, (200, 200))

    def attaquer(self, ennemi):
        degats = random.randint(5, 10)
        ennemi.vie -= degats
        print(f"{self.nom} attaque {ennemi.nom} et lui inflige {degats} dégâts.")

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
ecran = pygame.display.set_mode((900, 400))
pygame.display.set_caption("Pokémon Combat Simulator")
fond = pygame.image.load("image/arene.webp")
fond = pygame.transform.scale(fond, (900, 400))

# Choix du Pokémon
def choisir_pokemon():
    choix_effectue = False
    pokemon_choisi = None
    while not choix_effectue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pygame.Rect(50, 50, 200, 200).collidepoint(pos):
                    pokemon_choisi = pikachu
                elif pygame.Rect(250, 50, 200, 200).collidepoint(pos):
                    pokemon_choisi = bulbizarre
                elif pygame.Rect(450, 50, 200, 200).collidepoint(pos):
                    pokemon_choisi = salameche
                elif pygame.Rect(650, 50, 200, 200).collidepoint(pos):
                    pokemon_choisi = carapuce
                if pokemon_choisi:
                    choix_effectue = True
                    return pokemon_choisi

        ecran.blit(fond, (0, 0))
        ecran.blit(pikachu.image, (50, 50))
        ecran.blit(bulbizarre.image, (250, 50))
        ecran.blit(salameche.image, (450, 50))
        ecran.blit(carapuce.image, (650, 50))
        pygame.display.flip()

def choisir_adversaire(pokemon_joueur):
    adversaires = [pikachu, bulbizarre, salameche, carapuce]
    adversaires.remove(pokemon_joueur)
    return random.choice(adversaires)

pokemon_joueur = choisir_pokemon()
pokemon_adversaire = choisir_adversaire(pokemon_joueur)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pokemon_joueur.attaquer(pokemon_adversaire)

    ecran.blit(fond, (0, 0))
    ecran.blit(pokemon_joueur.image, (100, 50))  # Position du Pokémon du joueur
    ecran.blit(pokemon_adversaire.image, (700, 50))  # Position de l'adversaire
    pygame.display.flip()




