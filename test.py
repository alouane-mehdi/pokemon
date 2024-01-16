import pygame
import sys

class Personnage:
    def __init__(self, nom, vie, image_path, scale_factor=1):
        self.nom = nom
        self.vie = vie
        original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(original_image, (int(original_image.get_width() * scale_factor), int(original_image.get_height() * scale_factor)))
        self.rect = self.image.get_rect()
        self.x = 100  # Initial X position
        self.y = 300  # Initial Y position

    def attaquer(self, ennemi):
        ennemi.vie -= 5
        print(f"Vie de {ennemi.nom}: {ennemi.vie}")

    def __str__(self):
        return self.nom

class Jeu:
    def __init__(self):
        self.niveau = 1
        self.joueur = None
        self.ennemi = None

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1 facile, 2 moyen, 3 difficile) : "))

    def initialiserPersonnages(self):
        if self.niveau == 1:
            self.joueur = Personnage("Joueur", 13, "assets/bulbizarre.jpg", scale_factor=0.5)
            self.ennemi = Personnage("IA", 13, "assets/carapuce.jpg", scale_factor=0.5)
        elif self.niveau == 2:
            self.joueur = Personnage("Joueur", 23, "assets/bulbizarre.jpg", scale_factor=0.5)
            self.ennemi = Personnage("IA", 23, "assets/carapuce.jpg", scale_factor=0.5)
        elif self.niveau == 3:
            self.joueur = Personnage("Joueur", 33, "assets/bulbizarre.jpg", scale_factor=0.5)
            self.ennemi = Personnage("IA", 33, "assets/carapuce.jpg", scale_factor=0.5)

    def lancerJeu(self):
        pygame.init()
        clock = pygame.time.Clock()

        width, height = 800, 600
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Jeu 1v1")

        # Load arena image
        arena_image = pygame.image.load("assets/arene.png")
        arena_image = pygame.transform.scale(arena_image, (width, height))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.joueur.attaquer(self.ennemi)
                if self.ennemi.vie <= 0:
                    print(f"{self.ennemi.nom} n'a plus de vie ! {self.joueur.nom} remporte la victoire!")
                    pygame.quit()
                    sys.exit()

                self.ennemi.attaquer(self.joueur)
                if self.joueur.vie <= 0:
                    print(f"{self.joueur.nom} n'a plus de vie ! {self.ennemi.nom} remporte la victoire!")
                    pygame.quit()
                    sys.exit()

            # Draw arena
            screen.blit(arena_image, (0, 0))

            # Draw characters
            screen.blit(self.joueur.image, (self.joueur.x, self.joueur.y))


            pygame.display.flip()
            clock.tick(30)

if __name__ == "__main__":
    jeu = Jeu()
    jeu.choisirNiveau()
    jeu.initialiserPersonnages()
    jeu.lancerJeu()