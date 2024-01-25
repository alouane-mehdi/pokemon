import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Pokémon Battle Arena")

# Charger le fond d'écran
fond = pygame.image.load("/Users/boumediene/Desktop/Map/pokemon/assets/pokemonBack.jpeg")
fond = pygame.transform.scale(fond, (largeur, hauteur))

# Couleurs
blanc = (255, 255, 255)
jaune = (255, 255, 0)  # Jaune

# Police de texte
font = pygame.font.Font(None, 52)  # Diminuer la taille du texte

# Position verticale initiale du texte
position_y = hauteur // 2 - 30  # 30 est la moitié de la hauteur du texte

# Fonction pour afficher le texte à une position verticale donnée
def afficher_texte_position_y(texte, y):
    texte_surface = font.render(texte, True, jaune)
    texte_rect = texte_surface.get_rect(center=(largeur // 2, y))  # Centrer le texte horizontalement
    fenetre.blit(texte_surface, texte_rect)

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Afficher le fond d'écran
    fenetre.blit(fond, (0, 0))

    # Afficher le texte à la position verticale actuelle
    afficher_texte_position_y("Bienvenue dans la Pokémon Battle Arena !", position_y)
    afficher_texte_position_y("Choisissez votre Pokémon et combattez !", position_y + 50)
    afficher_texte_position_y("Appuyez sur 'ESPACE' pour attaquer", position_y + 100)
    afficher_texte_position_y("Appuyez sur 'R' pour recommencez une partie ", position_y + 150)
    afficher_texte_position_y("Appuyez sur 'Q' pour quitter la partie et retournez au menu principale", position_y + 200)
    afficher_texte_position_y("A la fin du comnat appuyez sur 'P' pour aller sur le pokedex", position_y + 250)
    # Incrémenter la position verticale pour déplacer le texte vers le haut
    position_y -= 1

    # Si le texte a atteint le haut de la fenêtre, réinitialiser la position
    if position_y + 100 < 0:
        position_y = hauteur

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Limiter la vitesse de la boucle
    pygame.time.Clock().tick(30)

# Quitter Pygame
pygame.quit()
sys.exit()

