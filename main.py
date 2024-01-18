import pygame
import sys
from button import Bouton
from syscombat import Jeu  

class PokemonMenu:
    def __init__(self):
        pygame.init()

        self.ÉCRAN = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Menu")

        self.FOND = pygame.image.load("assets/background.png")

        pygame.mixer.music.load("assets/musicfond.mp3")
        self.BRUIT_SURVOL = pygame.mixer.Sound("assets/sonbouton.flac")

        pygame.mixer.music.set_volume(0.5)
        self.BRUIT_SURVOL.set_volume(0.7)

    def obtenir_police(self, taille):
        return pygame.font.Font("assets/font.ttf", taille)
    def jouer(self):
        combat = Jeu()

        pygame.event.clear()  # Efface les événements en attente

        # Boucle pour choisir le niveau
        while combat.choix_niveau:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                combat.choisirNiveau(event)
                combat.initialiserPersonnages()
                combat.lancerJeu()

 
    def options(self):
        while True:
            POSITION_SOURIS_OPTIONS = pygame.mouse.get_pos()

            self.ÉCRAN.fill("white")

            TEXTE_OPTIONS = self.obtenir_police(45).render("C'est l'écran OPTIONS.", True, "Black")
            RECTANGLE_OPTIONS = TEXTE_OPTIONS.get_rect(center=(640, 260))
            self.ÉCRAN.blit(TEXTE_OPTIONS, RECTANGLE_OPTIONS)

            BOUTON_RETOUR_OPTIONS = Bouton(image=None, pos=(640, 460),
                                           text_input="RETOUR", font=self.obtenir_police(75), base_color="Black", hovering_color="Green")

            BOUTON_RETOUR_OPTIONS.changer_couleur(POSITION_SOURIS_OPTIONS)
            BOUTON_RETOUR_OPTIONS.mettre_a_jour(self.ÉCRAN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BOUTON_RETOUR_OPTIONS.verifier_input(POSITION_SOURIS_OPTIONS):
                        self.menu_principal()

            pygame.display.update()

    def menu_principal(self):
        pygame.mixer.music.play(-1)
        self.BRUIT_SURVOL.play(maxtime=0)

        while True:
            self.ÉCRAN.blit(self.FOND, (0, 0))

            POSITION_SOURIS_MENU = pygame.mouse.get_pos()

            TEXTE_MENU = self.obtenir_police(100).render("POKEMON", True, "#FFFF00")
            RECTANGLE_MENU = TEXTE_MENU.get_rect(center=(640, 100))

            self.ÉCRAN.blit(TEXTE_MENU, RECTANGLE_MENU)

            BOUTON_JOUER = Bouton(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                                  text_input="JOUER", font=self.obtenir_police(75), base_color="White", hovering_color="Blue", son_survol=self.BRUIT_SURVOL)
            BOUTON_OPTIONS = Bouton(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                    text_input="POKEDEX", font=self.obtenir_police(75), base_color="White", hovering_color="Blue", son_survol=self.BRUIT_SURVOL)
            BOUTON_QUITTER = Bouton(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                                     text_input="QUITTER", font=self.obtenir_police(75), base_color="White", hovering_color="Blue", son_survol=self.BRUIT_SURVOL)

            for bouton in [BOUTON_JOUER, BOUTON_OPTIONS, BOUTON_QUITTER]:
                bouton.changer_couleur(POSITION_SOURIS_MENU)
                bouton.mettre_a_jour(self.ÉCRAN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BOUTON_JOUER.verifier_input(POSITION_SOURIS_MENU):
                        pygame.mixer.music.stop()
                        self.jouer()
                    if BOUTON_OPTIONS.verifier_input(POSITION_SOURIS_MENU):
                        pygame.mixer.music.stop()
                        self.options()
                    if BOUTON_QUITTER.verifier_input(POSITION_SOURIS_MENU):
                        pygame.mixer.music.stop()
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

if __name__ == "__main__":
    menu = PokemonMenu()
    menu.menu_principal()
