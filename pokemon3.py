import pygame
import random

class Pokemon:
    def __init__(self, nom, type_pokemon, vie, description, chemin_image):
        self.nom = nom
        self.type = type_pokemon
        self.vie_max = vie
        self.vie = vie
        self.description = description
        self.chemin_image = chemin_image
        self.load_image()

    def load_image(self):
        # Charger et redimensionner l'image du Pokémon
        try:
            self.image = pygame.image.load(self.chemin_image)
            self.image = pygame.transform.scale(self.image, (200, 200))
        except pygame.error as e:
            print(f"Erreur lors du chargement de l'image {self.chemin_image}: {e}")
            self.image = None

    def to_dict(self):
        # Retourner un dictionnaire des attributs du Pokémon pour le Pokedex
        return {
            'nom': self.nom,
            'type': self.type,
            'vie_max': self.vie_max,
            'description': self.description,
            'chemin_image': self.chemin_image
        }

    def reinitialiser_vie(self):
        # Réinitialiser la vie du Pokémon à sa valeur maximale
        self.vie = self.vie_max

    def attaquer(self, ennemi):
        # Effectuer une attaque sur l'ennemi
        degats = random.randint(5, 10)  # Choisir des dégâts aléatoires pour cet exemple
        ennemi.vie -= degats
        print(f"{self.nom} attaque {ennemi.nom} et lui inflige {degats} dégâts.")


 



