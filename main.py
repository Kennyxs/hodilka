import pygame
import sprites
import maper
from settings import *
# stop = 1
# surface = pygame.display.set_mode((500, 500))
# image = pygame.image.load("playerpng.png")
# player = sprites.Clasprite(image)
# fps = pygame.time.Clock() 
# map = maper.Map("map.csv", 'mapstuff.png')
# print(map.list)


# while stop > 0:
#     events = pygame.event.get()
#     for e_now in events:
#         if e_now.type == pygame.constants.QUIT:
#             stop = -1
#     surface.fill((0,0,0))
#     player.draw(surface)
#     player.update()
#     pygame.display.update()
#     fps.tick(60)


class Game:
    def __init__(self, height,weidth, png, map, mappng) -> None:
        self.height = height
        self.weidth = weidth
        self.png = png
        self.map = map
        self.mappng = mappng
        self.surface = pygame.display.set_mode((self.height, self.weidth))
    def new(self):
        self.image = pygame.image.load(self.png)
        self.player = sprites.Clasprite(self.image,game)
        self.fps = pygame.time.Clock() 
        self.mapp = maper.Map(self.map, self.mappng)
        self.camera = maper.Camera(self.mapp.sizemapxe, self.mapp.sizemapye)
        self.spritemaplist = self.mapp.plitochnikkid
        
    def events(self):
        events = pygame.event.get()
        stop = 1
        for e_now in events:
            if e_now.type == pygame.constants.QUIT:
                stop = -1
            else:
                stop = 1
        return stop
    def update(self):
        self.player.update()
        self.camera.spy(self.player)
        pygame.display.update()

    def draw(self):
        self.surface.fill((0,0,0))
        for plitka in self.mapp.plitochnikkid:
            plitka.draw(self.surface, self.camera.newrectsprite(plitka.rect))
        self.player.draw(self.surface, self.camera.newrectsprite(self.player.rect))
    def run(self):
        stop = 1
        self.new()
        while stop > 0:
            stop = self.events()
            self.draw()
            self.update()
            self.fps.tick(60)

game = Game(WEIDTH, HIGHT, "playerpng.png", "map2.csv", 'mapstaff.png')
game.run()