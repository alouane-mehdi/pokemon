import pygame
import random
import sys

class Combat:
    def __init__(self, joueur, ennemis, ecran, fond):
        self.joueur = joueur
        self.ennemis = ennemis
        self.ecran = ecran
        self.fond = fond
        self.ennemi = None

    def choisir_ennemi(self):
        self.ennemi = random.choice(self.ennemis)

    def afficher_barre_de_vie(self, pokemon, position_x, position_y):
        vie_max = pokemon.vie_max  # Utilisez la vie maximale du Pokémon
        largeur_barre = 200
        barre_vie_rect = pygame.Rect(position_x, position_y, largeur_barre, 20)
        pygame.draw.rect(self.ecran, (255, 0, 0), barre_vie_rect)  # Barre de vie vide (rouge)

        vie_restante = max(0, int((pokemon.vie / vie_max) * largeur_barre))
        barre_vie_restante_rect = pygame.Rect(position_x, position_y, vie_restante, 20)
        pygame.draw.rect(self.ecran, (0, 255, 0), barre_vie_restante_rect)  # Barre de vie actuelle (verte)

    def pokemon_est_vaincu(self, pokemon):
        return pokemon.vie <= 0

    def lancer_combat(self):
        self.choisir_ennemi()
        police = pygame.font.Font(None, 36)  # Taille de la police
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.joueur.attaquer(self.ennemi)
                        self.afficher_barre_de_vie(self.ennemi, 700, 30)
                        pygame.display.flip()

                        if self.pokemon_est_vaincu(self.ennemi):
                            message = f"{self.joueur.nom} a gagné le combat!"
                            texte = police.render(message, True, (0, 0, 0))
                            self.ecran.blit(texte, (250, 200))
                            pygame.display.flip()
                            pygame.time.delay(5000)
                            return True  # Le joueur gagne

                        self.ennemi.attaquer(self.joueur)
                        self.afficher_barre_de_vie(self.joueur, 100, 30)
                        pygame.display.flip()

                        if self.pokemon_est_vaincu(self.joueur):
                            message = f"{self.ennemi.nom} a gagné le combat!"
                            texte = police.render(message, True, (0, 0, 0))
                            self.ecran.blit(texte, (250, 200))
                            pygame.display.flip()
                            pygame.time.delay(5000)
                            return True  # L'ennemi gagne

                # Mettre à jour l'affichage après chaque événement
                self.ecran.blit(self.fond, (0, 0))
                self.ecran.blit(self.joueur.image, (100, 50))
                self.ecran.blit(self.ennemi.image, (700, 50))
                self.afficher_barre_de_vie(self.joueur, 100, 30)
                self.afficher_barre_de_vie(self.ennemi, 700, 30)
                pygame.display.flip()

        return False  # Si le jeu est quitté

