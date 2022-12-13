import pygame as pg
import pygame.freetype





pygame.init()
screen = pg.display.set_mode((544, 256))

font = pygame.freetype.Font(None, 16)
image = pg.image.load('mapstaff.png')
image = pg.transform.scale(image, (544, 256))

index = 0
for y in range(0, 256, 32):
    for x in range(0, 544, 32):
        font.render_to(image, (x+10, y+10), str(index), fgcolor=(255, 255, 255))
        index += 1

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN
                                    and event.key == pg.K_ESCAPE):
            running = False
    screen.blit(image, (0, 0))
    pg.display.flip()

