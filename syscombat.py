import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_1, K_2, K_3, K_4
import random  

class Personnage:
    def __init__(self, nom, vie, image_path, degats, scale_factor=1):
        self.nom = nom
        self.vie = vie
        self.vie_max = vie
        self.degats = degats  # Ajout de l'attribut degats
        self.image = pygame.transform.scale(pygame.image.load(image_path),
                                            (int(50 * scale_factor), int(50 * scale_factor)))
        self.rect = self.image.get_rect()
        self.x = 100  
        self.y = 300  

    def attaquer(self, ennemi):
        ennemi.vie -= self.degats
        print(f"{self.nom} attaque {ennemi.nom} et lui inflige {self.degats} dégâts.")
        print(f"Vie de {ennemi.nom}: {ennemi.vie}")

    def afficher_barre_vie(self, screen):
        barre_vie_rect = pygame.Rect(self.x, self.y - 10, 50, 5)
        pygame.draw.rect(screen, (255, 0, 0), barre_vie_rect)  # Barre de vie rouge

        vie_restante = max(0, int((self.vie / self.vie_max) * 50))
        barre_vie_restante_rect = pygame.Rect(self.x, self.y - 10, vie_restante, 5)
        pygame.draw.rect(screen, (0, 255, 0), barre_vie_restante_rect)  # Barre de vie verte

    def __str__(self):
        return self.nom

class Jeu:
    def __init__(self):
        self.niveau = 1
        self.joueur = None
        self.ennemi = None
        self.choix_niveau = True  # Nouvelle variable pour gérer l'écran de choix du niveau
        
    def quitterJeu(self):
        pygame.quit()
        sys.exit()

    def revenirEcranSelection(self):
        self.niveau = 1
        self.joueur = None
        self.ennemi = None
        self.choix_niveau = True

    def afficher_choix_niveau(self, screen):
        screen.fill((255, 255, 255))

        police = pygame.font.Font(None, 36)
        texte = police.render("Choisissez votre personnage :", True, (0, 0, 0))
        rect_texte = texte.get_rect(center=(400, 100))
        screen.blit(texte, rect_texte)

        texte_pikachu = police.render("1. Pikachu", True, (0, 0, 0))
        rect_pikachu = texte_pikachu.get_rect(center=(400, 200))
        screen.blit(texte_pikachu, rect_pikachu)

        texte_carapuce = police.render("2. Carapuce", True, (0, 0, 0))
        rect_carapuce = texte_carapuce.get_rect(center=(400, 250))
        screen.blit(texte_carapuce, rect_carapuce)

        texte_salamèche = police.render("3. Salamèche", True, (0, 0, 0))
        rect_salamèche = texte_salamèche.get_rect(center=(400, 300))
        screen.blit(texte_salamèche, rect_salamèche)

        texte_bulbizarre = police.render("4. Bulbizarre", True, (0, 0, 0))
        rect_bulbizarre = texte_bulbizarre.get_rect(center=(400, 350))
        screen.blit(texte_bulbizarre, rect_bulbizarre)

    def afficher_arena(self, screen, arena_image):
        screen.blit(arena_image, (0, 0))

    def choisirNiveau(self, event):
        if event.type == KEYDOWN:
            if event.key == K_1:
                self.niveau = 1
                self.choix_niveau = False
                self.initialiserPersonnages()
            elif event.key == K_2:
                self.niveau = 2 
                self.choix_niveau = False
                self.initialiserPersonnages()
            elif event.key == K_3:
                self.niveau = 3
                self.choix_niveau = False
                self.initialiserPersonnages()
            elif event.key == K_4:
                self.niveau = 4
                self.choix_niveau = False
                self.initialiserPersonnages()

    def initialiserPersonnages(self):
        personnages_disponibles = [
            Personnage("Pikachu", 175, "assets/pikachu.png", degats=50, scale_factor=5),
            Personnage("Carapuce", 300, "assets/carapuce.jpg", degats=30, scale_factor=5),
            Personnage("Salamèche", 175, "assets/salameche.jpg", degats=50, scale_factor=5),
            Personnage("Bulbizarre", 250, "assets/bulbizarre.jpg", degats=30, scale_factor=5)
        ]

        choix_joueur = None

        while choix_joueur is None:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_1:
                        choix_joueur = "Pikachu"
                    elif event.key == K_2:
                        choix_joueur = "Carapuce"
                    elif event.key == K_3:
                        choix_joueur = "Salamèche"
                    elif event.key == K_4:
                        choix_joueur = "Bulbizarre"

        self.joueur = next(p for p in personnages_disponibles if p.nom == choix_joueur)

        # Sélection aléatoire de l'ennemi parmi les personnages restants
        personnages_restants = [p for p in personnages_disponibles if p != self.joueur]
        self.ennemi = random.choice(personnages_restants)

    def lancerJeu(self):
        pygame.init()
        clock = pygame.time.Clock()

        width, height = 800, 600
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Jeu 1v1")

        arena_image = pygame.image.load("assets/arene.png")
        arena_image = pygame.transform.scale(arena_image, (width, height))

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quitterJeu()
                elif self.choix_niveau:
                    self.choisirNiveau(event)

            if self.choix_niveau:
                self.afficher_choix_niveau(screen)
            else:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    self.joueur.attaquer(self.ennemi)
                    if self.ennemi.vie <= 0:
                        print(f"{self.ennemi.nom} n'a plus de vie ! {self.joueur.nom} remporte la victoire!")
                        self.revenirEcranSelection()

                    self.ennemi.attaquer(self.joueur)
                    if self.joueur.vie <= 0:
                        print(f"{self.joueur.nom} n'a plus de vie ! {self.ennemi.nom} remporte la victoire!")
                        self.revenirEcranSelection()

                self.afficher_arena(screen, arena_image)
                self.joueur.afficher_barre_vie(screen)
                screen.blit(self.joueur.image, (self.joueur.x, self.joueur.y))

                self.ennemi.x = width - self.ennemi.rect.width
                self.ennemi.y = 50

                self.ennemi.afficher_barre_vie(screen)
                screen.blit(self.ennemi.image, (self.ennemi.x, self.ennemi.y))

            pygame.display.flip()
            clock.tick(30)

if __name__ == "__main__":
    jeu = Jeu()
    jeu.lancerJeu()
