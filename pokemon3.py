import pygame
import random

class Pokemon:
    def __init__(self, nom, type_pokemon, vie, description, chemin_image):
        self.nom = nom
        self.type = type_pokemon
        self.vie_max = vie  # Ajoutez un attribut pour stocker la vie maximale
        self.vie = vie
        self.description = description
        self.image = pygame.image.load(chemin_image)
        self.image = pygame.transform.scale(self.image, (200, 200))

    def reinitialiser_vie(self):
        self.vie = self.vie_max    

    def attaquer(self, ennemi):
        degats = random.randint(5, 10)
        ennemi.vie -= degats
        print(f"{self.nom} attaque {ennemi.nom} et lui inflige {degats} dégâts.")
