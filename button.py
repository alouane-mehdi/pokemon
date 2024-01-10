import pygame

class Bouton():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color, son_survol):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.couleur_base, self.couleur_survol = base_color, hovering_color
        self.texte_input = text_input
        self.texte = self.font.render(self.texte_input, True, self.couleur_base)
        if self.image is None:
            self.image = self.texte
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.rect_texte = self.texte.get_rect(center=(self.x_pos, self.y_pos))
        self.son_survol = son_survol

    def mettre_a_jour(self, écran):
        if self.image is not None:
            écran.blit(self.image, self.rect)
        écran.blit(self.texte, self.rect_texte)

    def verifier_input(self, position):
        return self.rect.collidepoint(position)

    def jouer_son_survol(self):
        pygame.mixer.Sound.play(self.son_survol)

    def changer_couleur(self, position):
        if self.rect.collidepoint(position):
            self.texte = self.font.render(self.texte_input, True, self.couleur_survol)
            self.jouer_son_survol()
        else:
            self.texte = self.font.render(self.texte_input, True, self.couleur_base)
