import pygame
import sys
from pokemon3 import Pokemon
from combat3 import Combat

class PokemonGame:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("music/street-fight.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        pikachu = Pokemon("Pikachu", "Électrique", 30, "Célèbre pour ses joues électriques.", "image/pikachu.png")
        bulbizarre = Pokemon("Bulbizarre", "Plante/Poison", 35, "Possède une plante sur son dos.", "image/bulbizarre.png")
        salameche = Pokemon("Salameche", "Feu", 33, "Sa queue est enflammée quand il est en bonne santé.", "image/salameche.png")
        carapuce = Pokemon("Carapuce", "Eau", 32, "Un petit Pokémon tortue.", "image/carapuce.png")

        self.ecran = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Pokémon Combat Simulator")
        self.fond = pygame.image.load("image/arene.webp")
        self.fond = pygame.transform.scale(self.fond, (1280, 720))

        self.pokemons = [pikachu, bulbizarre, salameche, carapuce]

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

    def run_game(self):
        while True:
            pokemon_joueur = self.choisir_pokemon()
            ennemis_potentiels = [p for p in self.pokemons if p != pokemon_joueur]
            combat = Combat(pokemon_joueur, ennemis_potentiels, self.ecran, self.fond)
            fin_combat = combat.lancer_combat()

            
            pokemon_joueur.reinitialiser_vie()
            for ennemi in ennemis_potentiels:
                ennemi.reinitialiser_vie()

            if not fin_combat:
                break  

            
            prompt_text = "Appuyez sur 'r' pour relancer un combat ou 'q' pour quitter."
            font = pygame.font.Font(None, 36)
            prompt_surface = font.render(prompt_text, True, (255, 255, 255))
            prompt_rect = prompt_surface.get_rect(center=(self.ecran.get_width() // 2, self.ecran.get_height() - 50))

            pygame.display.flip()

            relaunch = False
            while not relaunch:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:  
                            relaunch = True
                        elif event.key == pygame.K_q:  
                            pygame.quit()
                            sys.exit()

                self.ecran.blit(self.fond, (0, 0))
                self.ecran.blit(prompt_surface, prompt_rect)
                pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = PokemonGame()
    game.run_game()
