import pygame
import sys

class PokemonBattleArena:
    def __init__(self):
        # Initialisation de Pygame
        pygame.init()

        # Paramètres de la fenêtre
        self.largeur, self.hauteur = 1280, 720
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Pokémon Battle Arena")

        # Charger le fond d'écran
        self.fond = pygame.image.load("assets/pokemonBack.jpeg")
        self.fond = pygame.transform.scale(self.fond, (self.largeur, self.hauteur))

        # Couleurs
        self.blanc = (255, 255, 255)
        self.jaune = (255, 255, 0)  # Jaune

        # Police de texte
        self.font = pygame.font.Font(None, 24)  # Diminuer la taille du texte

        # Position verticale initiale du texte
        self.position_y = self.hauteur // 2 - 30  # 30 est la moitié de la hauteur du texte

        # Boucle principale du jeu
        self.running = True

    def afficher_texte_position_y(self, texte, y):
        texte_surface = self.font.render(texte, True, self.jaune)
        texte_rect = texte_surface.get_rect(center=(self.largeur // 2, y))
        self.fenetre.blit(texte_surface, texte_rect)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Afficher le fond d'écran
            self.fenetre.blit(self.fond, (0, 0))

            # Afficher le texte à la position verticale actuelle
            self.afficher_texte_position_y("Bienvenue dans la Pokémon Battle Arena !", self.position_y)
            self.afficher_texte_position_y("Choisissez votre Pokémon et combattez !", self.position_y + 50)
            self.afficher_texte_position_y("Appuyez sur 'ESPACE' pour attaquer", self.position_y + 100)
            self.afficher_texte_position_y("Appuyez sur 'R' pour recommencer une partie", self.position_y + 150)
            self.afficher_texte_position_y("Appuyez sur 'Q' pour quitter la partie et retournez au menu principal", self.position_y + 200)

            # Incrémenter la position verticale pour déplacer le texte vers le haut
            self.position_y -= 1

            # Si le texte a atteint le haut de la fenêtre, réinitialiser la position
            if self.position_y + 100 < 0:
                self.position_y = self.hauteur

            # Mise à jour de l'affichage
            pygame.display.flip()

            # Limiter la vitesse de la boucle
            pygame.time.Clock().tick(30)

        # Quitter Pygame
        pygame.quit()
        sys.exit()

# Créer une instance de la classe et exécuter le jeu
if __name__ == "__main__":
    jeu = PokemonBattleArena()
    jeu.run()



