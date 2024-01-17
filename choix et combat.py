import pygame
import sys
import random

# Classe Personnage pour gérer les Pokémon
class Personnage:
    def __init__(self, nom, type_pokemon, vie, description, image_path):
        self.nom = nom
        self.type = type_pokemon
        self.description = description
        self.vie = vie
        self.vie_max = vie
        self.image = pygame.transform.scale(pygame.image.load(image_path), (100, 100))
        self.x = 100  # Position initiale
        self.y = 300  # Position initiale

    def attaquer(self, ennemi):
        degats = random.randint(5, 10)
        ennemi.vie -= degats
        print(f"{self.nom} attaque {ennemi.nom} et lui inflige {degats} dégâts.")

    def afficher_barre_vie(self, screen):
        barre_vie_totale = pygame.Rect(self.x, self.y - 20, 100, 10)
        pygame.draw.rect(screen, (255, 0, 0), barre_vie_totale)
        vie_restante = max(0, int((self.vie / self.vie_max) * 100))
        barre_vie_restante = pygame.Rect(self.x, self.y - 20, vie_restante, 10)
        pygame.draw.rect(screen, (0, 255, 0), barre_vie_restante)

# Classe principale du jeu
class Jeu:
    def __init__(self):
        self.personnages = [
            Personnage("Pikachu", "Électrique", 30, "Célèbre pour ses joues électriques.", "image/pikachu.png"),
            Personnage("Bulbizarre", "Plante/Poison", 35, "Possède une plante sur son dos.", "image/bulbizarre.png"),
            Personnage("Salameche", "Feu", 33, "Sa queue est enflammée quand il est en bonne santé.", "image/salameche.png"),
            Personnage("Carapuce", "Eau", 32, "Un petit Pokémon tortue.", "image/carapuce.png")
        ]
        self.joueur = None
        self.ennemi = None
        self.choix_personnage = True
        self.ecran = pygame.display.set_mode((800, 600))

    def choisir_personnage(self):
        self.ecran.fill((255, 255, 255))
        police = pygame.font.SysFont(None, 40)
        y = 100
        for index, perso in enumerate(self.personnages):
            texte = police.render(f"{index + 1}. {perso.nom}", True, (0, 0, 0))
            self.ecran.blit(texte, (100, y))
            y += 50
        pygame.display.flip()

        attente_choix = True
        while attente_choix:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.joueur = self.personnages[0]
                        attente_choix = False
                    elif event.key == pygame.K_2:
                        self.joueur = self.personnages[1]
                        attente_choix = False
                    elif event.key == pygame.K_3:
                        self.joueur = self.personnages[2]
                        attente_choix = False
                    elif event.key == pygame.K_4:
                        self.joueur = self.personnages[3]
                        attente_choix = False

    def lancerJeu(self):
        pygame.init()
        pygame.display.set_caption("Pokémon Combat Simulator")

        self.choisir_personnage()

        # Initialisation du combat
        self.ennemi = random.choice([p for p in self.personnages if p != self.joueur])
        self.ennemi.x, self.ennemi.y = 600, 300

        # Boucle principale du combat
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.joueur.attaquer(self.ennemi)
                    if self.ennemi.vie <= 0:
                        print(f"{self.ennemi.nom} est vaincu! {self.joueur.nom} remporte la victoire!")
                        pygame.quit()
                        sys.exit()
                    self.ennemi.attaquer(self.joueur)
                    if self.joueur.vie <= 0:
                        print(f"{self.joueur.nom} est vaincu! {self.ennemi.nom} remporte la victoire!")
                        pygame.quit()
                        sys.exit()

            self.ecran.fill((255, 255, 255))
            self.joueur.afficher_barre_vie(self.ecran)
            self.ennemi.afficher_barre_vie(self.ecran)
            self.ecran.blit(self.joueur.image, (self.joueur.x, self.joueur.y))
            self.ecran.blit(self.ennemi.image, (self.ennemi.x, self.ennemi.y))
            pygame.display.flip()

if __name__ == "__main__":
    jeu = Jeu()
    jeu.lancerJeu()

