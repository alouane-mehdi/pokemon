import pygame

pygame.init()

pygame.display.set_caption("Aréne 1")
screen = pygame.display.set_mode((600, 400))
background = pygame.image.load('assets/bgarene.jpeg')


mini_image_original = pygame.image.load('assets/salameche.png')
mini_image_size = (100, 100) 
mini_image = pygame.transform.scale(mini_image_original, mini_image_size)


screen_width, screen_height = screen.get_size()


mini_width, mini_height = mini_image.get_size()


mini_image_x = screen_width - mini_width - 10  
mini_image_y = screen_height - mini_height - 10 



running = True

while running:
    screen.blit(background, (10, 50))

   
    screen.blit(mini_image, (mini_image_x, mini_image_y))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu ")


