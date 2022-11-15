import pygame
import sprites
stop = 1
surface = pygame.display.set_mode((350, 350))
image = pygame.image.load("playerpng.png")
player = sprites.Clasprite(image)





while stop > 0:
    events = pygame.event.get()
    for e_now in events:
        if e_now.type == pygame.constants.QUIT:
            stop = -1
    player.draw(surface)
    player.update()
    pygame.display.update()