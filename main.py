import pygame
import sprites

stop = 1
surface = pygame.display.set_mode((500, 500))
image = pygame.image.load("playerpng.png")
player = sprites.Clasprite(image)
fps = pygame.time.Clock()




while stop > 0:
    events = pygame.event.get()
    for e_now in events:
        if e_now.type == pygame.constants.QUIT:
            stop = -1
    surface.fill((0,0,0))
    player.draw(surface)
    player.update()
    pygame.display.update()
    fps.tick(60)