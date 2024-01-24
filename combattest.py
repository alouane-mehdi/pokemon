# combattest.py
import pygame
import sys
from pokemon3 import Pokemon
from combat3 import Combat

class PokemonGame:
    def __init__(self):
        pygame.init()

        self.ecran = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Pokémon Combat Simulator")
        self.fond = pygame.image.load("image/arene.webp")
        self.fond = pygame.transform.scale(self.fond, (1280, 720))

        self.pokemons = [
            Pokemon("Pikachu", "Électrique", 30, "Célèbre pour ses joues électriques.", "image/pikachu.png"),
            Pokemon("Bulbizarre", "Plante/Poison", 35, "Possède une plante sur son dos.", "image/bulbizarre.png"),
            Pokemon("Salameche", "Feu", 33, "Sa queue est enflammée quand il est en bonne santé.", "image/salameche.png"),
            Pokemon("Carapuce", "Eau", 32, "Un petit Pokémon tortue.", "image/carapuce.png")
        ]

    def choisir_pokemon(self):
        pokemon_width = 200
        spacing = 50
        total_width = pokemon_width * len(self.pokemons) + spacing * (len(self.pokemons) - 1)
        start_x = (self.ecran.get_width() - total_width) // 2

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for i, pokemon in enumerate(self.pokemons):
                        if pygame.Rect(start_x + i * (pokemon_width + spacing), 50, pokemon_width, 200).collidepoint(pos):
                            return pokemon

            self.ecran.blit(self.fond, (0, 0))
            for i, pokemon in enumerate(self.pokemons):
                self.ecran.blit(pokemon.image, (start_x + i * (pokemon_width + spacing), 50))
            pygame.display.flip()

    def afficher_menu(self):
        font = pygame.font.Font(None, 36)
        menu_texte = font.render("Appuyez sur 'R' pour relancer un combat ou 'Q' pour quitter", True, (255, 255, 255))
        self.ecran.blit(menu_texte, ((self.ecran.get_width() - menu_texte.get_width()) // 2, 600))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return True
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

    def lancer_combat(self):
        while True:
            pokemon_joueur = self.choisir_pokemon()
            ennemis_potentiels = [p for p in self.pokemons if p != pokemon_joueur]
            combat = Combat(pokemon_joueur, ennemis_potentiels, self.ecran, self.fond, self.afficher_menu)
            fin_combat = combat.lancer_combat()

            pokemon_joueur.reinitialiser_vie()
            for ennemi in ennemis_potentiels:
                ennemi.reinitialiser_vie()

            if not fin_combat:
                return

            if not self.afficher_menu():
                return

if __name__ == "__main__":
    game = PokemonGame()
    game.lancer_combat()

