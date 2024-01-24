import pygame
import sys
from button import Bouton
from combat3 import Combat  # Assurez-vous que le nom du fichier est correct
from combattest import choisir_pokemon  # Assurez-vous que le nom du fichier est correct

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

    def choisir_pokemon(self):
        # Utilisez la fonction du deuxième code pour obtenir le Pokémon du joueur
        pokemons = [...]  # Remplacez ceci par la liste de vos Pokémon
        ecran_combat = pygame.display.set_mode((950, 400))
        fond_combat = pygame.image.load("image/arene.webp")
        fond_combat = pygame.transform.scale(fond_combat, (950, 400))
        return choisir_pokemon(pokemons, ecran_combat, fond_combat)

    def lancer_combat(self):
        pokemon_joueur = self.choisir_pokemon()
        ennemis_potentiels = [p for p in pokemons if p != pokemon_joueur]
        combat = Combat(pokemon_joueur, ennemis_potentiels, ecran_combat, fond_combat)
        fin_combat = combat.lancer_combat()

        # Réinitialisez la vie des Pokémon après le combat
        pokemon_joueur.reinitialiser_vie()
        for ennemi in ennemis_potentiels:
            ennemi.reinitialiser_vie()

        if not fin_combat:
            pygame.quit()
            sys.exit()

    def options(self):
        while True:
           

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
                        self.lancer_combat()  # Appelle la méthode de lancement de combat
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
