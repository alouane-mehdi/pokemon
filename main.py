import pygame
import sys
from button import Bouton

pygame.init()

ÉCRAN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

FOND = pygame.image.load("assets/background.png")

def obtenir_police(taille):  
    return pygame.font.Font("assets/font.ttf", taille)

# Charger les musiques
pygame.mixer.music.load("assets/musicfond.mp3")
BRUIT_SURVOL = pygame.mixer.Sound("assets/sonbouton.flac")

# Définir le volume initial des musiques
pygame.mixer.music.set_volume(0.5)  # Volume de la musique de fond
BRUIT_SURVOL.set_volume(0.7)  # Volume du son de survol des boutons

def jouer():
    while True:
        POSITION_SOURIS = pygame.mouse.get_pos()

        ÉCRAN.fill("black")

        TEXTE_JOUER = obtenir_police(45).render("C'est l'écran de JEU.", True, "White")
        RECTANGLE_JOUER = TEXTE_JOUER.get_rect(center=(640, 260))
        ÉCRAN.blit(TEXTE_JOUER, RECTANGLE_JOUER)

        BOUTON_RETOUR = Bouton(image=None, pos=(640, 460),
                               text_input="RETOUR", font=obtenir_police(75), base_color="White", hovering_color="Green")

        BOUTON_RETOUR.changer_couleur(POSITION_SOURIS)
        BOUTON_RETOUR.mettre_a_jour(ÉCRAN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BOUTON_RETOUR.verifier_input(POSITION_SOURIS):
                    menu_principal()

        pygame.display.update()


def options():
    while True:
        POSITION_SOURIS_OPTIONS = pygame.mouse.get_pos()

        ÉCRAN.fill("white")

        TEXTE_OPTIONS = obtenir_police(45).render("C'est l'écran OPTIONS.", True, "Black")
        RECTANGLE_OPTIONS = TEXTE_OPTIONS.get_rect(center=(640, 260))
        ÉCRAN.blit(TEXTE_OPTIONS, RECTANGLE_OPTIONS)

        BOUTON_RETOUR_OPTIONS = Bouton(image=None, pos=(640, 460),
                                       text_input="RETOUR", font=obtenir_police(75), base_color="Black", hovering_color="Green")

        BOUTON_RETOUR_OPTIONS.changer_couleur(POSITION_SOURIS_OPTIONS)
        BOUTON_RETOUR_OPTIONS.mettre_a_jour(ÉCRAN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BOUTON_RETOUR_OPTIONS.verifier_input(POSITION_SOURIS_OPTIONS):
                    menu_principal()

        pygame.display.update()


def menu_principal():
    pygame.mixer.music.play(-1)  # Boucler indéfiniment
    BRUIT_SURVOL.play(maxtime=0)
    
    while True:
        ÉCRAN.blit(FOND, (0, 0))

        POSITION_SOURIS_MENU = pygame.mouse.get_pos()

        TEXTE_MENU = obtenir_police(100).render("POKEMON", True, "#FFFF00")
        RECTANGLE_MENU = TEXTE_MENU.get_rect(center=(640, 100))

        ÉCRAN.blit(TEXTE_MENU, RECTANGLE_MENU)

        BOUTON_JOUER = Bouton(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                              text_input="JOUER", font=obtenir_police(75), base_color="White", hovering_color="Blue", son_survol=BRUIT_SURVOL)
        BOUTON_OPTIONS = Bouton(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="POKEDEX", font=obtenir_police(75), base_color="White", hovering_color="Blue", son_survol=BRUIT_SURVOL)
        BOUTON_QUITTER = Bouton(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                                text_input="QUITTER", font=obtenir_police(75), base_color="White", hovering_color="Blue", son_survol=BRUIT_SURVOL)

        ÉCRAN.blit(TEXTE_MENU, RECTANGLE_MENU)

        for bouton in [BOUTON_JOUER, BOUTON_OPTIONS, BOUTON_QUITTER]:
            bouton.changer_couleur(POSITION_SOURIS_MENU)
            bouton.mettre_a_jour(ÉCRAN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()  # Arrêter la musique avant de quitter
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BOUTON_JOUER.verifier_input(POSITION_SOURIS_MENU):
                    pygame.mixer.music.stop()  # Arrêter la musique avant la transition
                    jouer()
                if BOUTON_OPTIONS.verifier_input(POSITION_SOURIS_MENU):
                    pygame.mixer.music.stop()
                    options()
                if BOUTON_QUITTER.verifier_input(POSITION_SOURIS_MENU):
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    menu_principal()



