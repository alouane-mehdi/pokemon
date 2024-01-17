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

# Initialisation du module mixer pour la musique
pygame.mixer.init()

# Charger et jouer la musique de fond
pygame.mixer.music.load("music/street-fight.mp3")  # Remplacez par le chemin de votre fichier de musique
pygame.mixer.music.set_volume(0.5)  # Réglez le volume (0.0 à 1.0)
pygame.mixer.music.play(-1)  # -1 signifie que la musique jouera en boucle

# Création des Pokémon
pikachu = Pokemon("Pikachu", "Électrique", 30, "Célèbre pour ses joues électriques.", "image/pikachu.png")
bulbizarre = Pokemon("Bulbizarre", "Plante/Poison", 35, "Possède une plante sur son dos.", "image/bulbizarre.png")
salameche = Pokemon("Salameche", "Feu", 33, "Sa queue est enflammée quand il est en bonne santé.", "image/salameche.png")
carapuce = Pokemon("Carapuce", "Eau", 32, "Un petit Pokémon tortue.", "image/carapuce.png")

# Création de la fenêtre principale
ecran = pygame.display.set_mode((900, 400))
pygame.display.set_caption("Pokémon Combat Simulator")

# Charger l'image de fond
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

pokemon_joueur = choisir_pokemon()

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Ici, vous pouvez définir la logique d'attaque ou d'interaction du Pokémon
                pokemon_joueur.attaquer(bulbizarre)  # Exemple d'attaque sur Bulbizarre

    # Mise à jour de l'affichage si nécessaire
    ecran.blit(fond, (0, 0))
    ecran.blit(pokemon_joueur.image, (50, 50))  # Affichage du Pokémon choisi
    # Afficher d'autres éléments si nécessaire
    pygame.display.flip()


