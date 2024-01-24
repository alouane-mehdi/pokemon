import pygame
import random

class Pokemon:
    def __init__(self, nom, type, vie_max, description, image_path):
        self.nom = nom
        self.type = type
        self.vie_max = vie_max
        self.vie = vie_max
        self.description = description
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (200, 200))

    def attaquer(self, ennemi):
        degats = random.randint(5, 10)
        ennemi.vie -= degats
        print(f"{self.nom} attaque {ennemi.nom} et lui inflige {degats} dégâts.")
        
    def reinitialiser_vie(self):
        self.vie = self.vie_max
