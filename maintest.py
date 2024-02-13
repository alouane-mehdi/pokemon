# combattest.py

import pygame
import sys
from button import Bouton
from tuto import Regles 
from combattest import PokemonGame  

class MenuPrincipal:
    def __init__(self, pokemon_game_class):
        self.pokemon_game_class = pokemon_game_class

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

    def options(self):
        while True:
            POSITION_SOURIS_OPTIONS = pygame.mouse.get_pos()
            
            regles = Regles()
            regles.run()

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
                        return
            pygame.display.update()

    def jouer(self):
        pygame.mixer.music.stop()
        game = self.pokemon_game_class()
        game.run()
        

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
                                  text_input="JOUER", font=self.obtenir_police(75), base_color="White", hovering_color="Blue")
            BOUTON_OPTIONS = Bouton(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                    text_input="REGLES", font=self.obtenir_police(75), base_color="White", hovering_color="Blue")
            BOUTON_QUITTER = Bouton(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                                    text_input="QUITTER", font=self.obtenir_police(75), base_color="White", hovering_color="Blue")
            self.ÉCRAN.blit(TEXTE_MENU, RECTANGLE_MENU)

            for bouton in [BOUTON_JOUER, BOUTON_OPTIONS, BOUTON_QUITTER]:
                bouton.changer_couleur(POSITION_SOURIS_MENU)
                bouton.mettre_a_jour(self.ÉCRAN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if BOUTON_JOUER.verifier_input(POSITION_SOURIS_MENU):
                        self.jouer()
                    elif BOUTON_OPTIONS.verifier_input(POSITION_SOURIS_MENU):
                        self.options()
                    elif BOUTON_QUITTER.verifier_input(POSITION_SOURIS_MENU):
                        pygame.mixer.music.stop()
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

if __name__ == "__main__":
    from combattest import PokemonGame
    menu_principal = MenuPrincipal(PokemonGame)
    menu_principal.menu_principal()
