import pygame
import sys

class SelectionPersonnage:
    def __init__(self):
        pygame.init()

        # Définir la taille de la fenêtre
        self.largeur, self.hauteur = 800, 600
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Sélection de Personnage")

        # Couleurs
        self.blanc = (255, 255, 255)
        self.noir = (0, 0, 0)
        self.rouge = (255, 0, 0)

        # Charger les images des personnages
        self.personnage1_img = pygame.image.load("assets/bulbizarre.jpg")
        self.personnage2_img = pygame.image.load("assets/carapuce.jpg")
        self.personnage3_img = pygame.image.load("assets/pikachu.png")
        self.personnage4_img = pygame.image.load("assets/salameche.jpg")

        # Redimensionner les images si nécessaire
        self.personnage1_img = pygame.transform.scale(self.personnage1_img, (150, 150))
        self.personnage2_img = pygame.transform.scale(self.personnage2_img, (150, 150))
        self.personnage3_img = pygame.transform.scale(self.personnage3_img, (150, 150))
        self.personnage4_img = pygame.transform.scale(self.personnage4_img, (150, 150))

        # Liste des personnages
        self.personnages = [self.personnage1_img, self.personnage2_img, self.personnage3_img, self.personnage4_img]
        self.personnage_actuel = 0

    def gestion_evenements(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Gestion des touches pour sélectionner le personnage
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.personnage_actuel = (self.personnage_actuel - 1) % len(self.personnages)
                elif event.key == pygame.K_RIGHT:
                    self.personnage_actuel = (self.personnage_actuel + 1) % len(self.personnages)

    def afficher_personnages(self):
        self.fenetre.fill(self.noir)

        for i, personnage in enumerate(self.personnages):
            x = (i + 1) * 150  # Espacement des personnages
            y = self.hauteur // 2
            self.fenetre.blit(personnage, (x - 50, y - 50))

            # Affichage de la sélection
            if i == self.personnage_actuel:
                pygame.draw.rect(self.fenetre, self.rouge, (x - 55, y - 55, 160, 160), 2)

    def boucle_principale(self):
        while True:
            self.gestion_evenements()
            self.afficher_personnages()

            pygame.display.flip()

if __name__ == "__main__":
    selection_personnage = SelectionPersonnage()
    selection_personnage.boucle_principale()

