import pygame
import sys
from combat import Jeu

# Définition de la classe Pokemon
class Pokemon:
    def __init__(self, nom, type_pokemon, description, chemin_image):
        self.nom = nom
        self.type = type_pokemon
        self.description = description
        self.image = pygame.image.load(chemin_image)
        self.image = pygame.transform.scale(self.image, (200, 200))

# Initialisation de Pygame
pygame.init()

# Initialisation du module mixer pour la musique
pygame.mixer.init()

# Charger et jouer la musique de fond
pygame.mixer.music.load("music/street-fight.mp3")  # Remplacez par le chemin de votre fichier de musique
pygame.mixer.music.set_volume(0.5)  # Réglez le volume (0.0 à 1.0)
pygame.mixer.music.play(-1)  # -1 signifie que la musique jouera en boucle

# Création des Pokémon
pikachu = Pokemon("Pikachu", "Électrique", "Célèbre pour ses joues électriques.", "image/pikachu.png")
bulbizarre = Pokemon("Bulbizarre", "Plante/Poison", "Possède une plante sur son dos.", "image/Bulbizarre.png")
salameche = Pokemon("Salameche", "Feu", "Sa queue est enflammée quand il est en bonne santé.", "image/salameche.png")
carapuce = Pokemon("Carapuce", "Eau", "Un petit Pokémon tortue.", "image/carapuce.png")

# Création de la fenêtre principale
ecran = pygame.display.set_mode((900, 400))
pygame.display.set_caption("Pokémon Combat Simulator")

# Charger l'image de fond
fond = pygame.image.load("image/arene.webp")
fond = pygame.transform.scale(fond, (900, 400))

# Fonction pour afficher les détails d'un Pokémon
def afficher_details_pokemon(pokemon):
    fenetre_details = pygame.display.set_mode((400, 400))
    pygame.display.set_caption(pokemon.nom)

    font = pygame.font.Font(None, 22)
    texte_description = font.render(pokemon.description, True, (0, 0, 0))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        fenetre_details.fill((255, 255, 255))
        fenetre_details.blit(pokemon.image, (100, 50))
        fenetre_details.blit(texte_description, (10, 260))

        pygame.display.flip()

    pygame.display.set_mode((900, 400))

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pygame.Rect(50, 50, 200, 200).collidepoint(pos):
                afficher_details_pokemon(pikachu)
            elif pygame.Rect(250, 50, 200, 200).collidepoint(pos):
                afficher_details_pokemon(bulbizarre)
            elif pygame.Rect(450, 50, 200, 200).collidepoint(pos):
                afficher_details_pokemon(salameche)
            elif pygame.Rect(650, 50, 200, 200).collidepoint(pos):
                afficher_details_pokemon(carapuce)
               

    # Dessiner le fond d'écran et les images des Pokémon
    ecran.blit(fond, (0, 0))
    ecran.blit(pikachu.image, (50, 50))
    ecran.blit(bulbizarre.image, (250, 50))
    ecran.blit(salameche.image, (450, 50))
    ecran.blit(carapuce.image, (650, 50))

    pygame.display.flip()


