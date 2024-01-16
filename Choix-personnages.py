import pygame
import sys

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

# Création des Pokémon
pikachu = Pokemon("Pikachu", "Électrique", "Célèbre pour ses joues électriques.", "image/pikachu.png")
bulbizarre = Pokemon("Bulbizarre", "Plante/Poison", "Possède une plante sur son dos.", "image/Bulbizarre.png")
salameche = Pokemon("Salameche", "Feu", "Sa queue est enflammée quand il est en bonne santé.", "image/salameche.png")
carapuce = Pokemon("Carapuce", "Eau", "Un petit Pokémon tortue.", "image/carapuce.png")

# Création de la fenêtre principale
ecran = pygame.display.set_mode((900, 400))
pygame.display.set_caption("Pokémon Combat Simulator")

# Charger l'image de fond
fond = pygame.image.load("image/arene.webp")  # Remplacez par le chemin de votre image
fond = pygame.transform.scale(fond, (900, 400))  # Redimensionner l'image pour qu'elle corresponde à la taille de la fenêtre

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

        fenetre_details.fill((255, 255, 255))  # Fond blanc
        fenetre_details.blit(pokemon.image, (100, 50))  # Afficher l'image du Pokémon
        fenetre_details.blit(texte_description, (10, 260))  # Afficher la description

        pygame.display.flip()

    pygame.display.set_mode((900, 400))  # Restaurer la taille de la fenêtre principale

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
