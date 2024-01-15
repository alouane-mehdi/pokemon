import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définir la taille de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Sélection de Personnage")

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (255, 0, 0)
vert = (0, 255, 0)

# Charger les images des personnages
personnage1_img = pygame.image.load("assets/bulbizarre.jpg")  # Remplacez "personnage1.png" par le chemin de votre image
personnage2_img = pygame.image.load("assets/carapuce.jpg")
personnage3_img = pygame.image.load("assets/pikachu.png")
personnage4_img = pygame.image.load("assets/salameche.jpg")

# Redimensionner les images si nécessaire
personnage1_img = pygame.transform.scale(personnage1_img, (150, 150))
personnage2_img = pygame.transform.scale(personnage2_img, (150, 150))
personnage3_img = pygame.transform.scale(personnage3_img, (150, 150))
personnage4_img = pygame.transform.scale(personnage4_img, (150, 150))

# Liste des personnages
personnages = [personnage1_img, personnage2_img, personnage3_img, personnage4_img]
personnage_actuel = 0


def afficher_pokemon_choisi(personnage_index):
    fenetre_pokemon = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("Pokemon Choisi")

    pokemon_choisi = pygame.transform.scale(personnages[personnage_index], (largeur, hauteur))
    
    fenetre_pokemon.blit(pokemon_choisi, (0, 0))
    pygame.display.flip()
# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Gestion des touches pour sélectionner le personnage
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                personnage_actuel = (personnage_actuel - 1) % len(personnages)
            elif event.key == pygame.K_RIGHT:
                personnage_actuel = (personnage_actuel + 1) % len(personnages)
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic gauche
                    afficher_pokemon_choisi(personnage_actuel)
    

    # Affichage des personnages et de la sélection
    fenetre.fill(noir)
    for i, personnage in enumerate(personnages):
        x = (i + 1) * 150  # Espacement des personnages
        y = hauteur // 2
        fenetre.blit(personnage, (x - 50, y - 50))

        # Affichage de la sélection
        if i == personnage_actuel:
            pygame.draw.rect(fenetre, rouge, (x - 55, y - 55, 160, 160), 2)

    pygame.display.flip()
