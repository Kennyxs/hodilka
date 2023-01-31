import pygame
import sprites
import maper
from settings import *
pygame.init()
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
        self.npc = sprites.Speaker(250,150,self.mapp.imlist[121],None,1,self)
        self.ivlnpc = sprites.evilnpc(500,300,self.mapp.imlist[125],self)
        self.weapontree = sprites.Weapontree(200,200,self.mapp.imlist[118], self)
        self.group = sprites.Group()
        self.test_event = pygame.USEREVENT
        pygame.time.set_timer(self.test_event, 500)
        self.tick = 1
    def neprozrach(self):
        a =abs(self.player.rect.x - self.ivlnpc.rect.x)
        b = abs(self.player.rect.y - self.ivlnpc.rect.y)
        c = (a*a+b*b)**0.5
        for t in self.mapp.plitochnikkid:
            d =abs(self.player.rect.x - t.rect.x)
            e = abs(self.player.rect.y - t.rect.y)
            f = (d*d+e*e)**0.5
            if c<200 and f>70:
                t.noprozrachno = 0
                
            else:
                
                if t.noprozrachno >20:
                    t.noprozrachno -= 10
                else:
                    t.noprozrachno = 0
        if c>70 and c<200:
            self.ivlnpc.wanish = 250
        else:
            if self.ivlnpc.wanish >5:
                self.ivlnpc.wanish -=5
            else: 
                self.ivlnpc.wanish = 0    

    def events(self):
        events = pygame.event.get()
        stop = 1
        for e_now in events:
            if e_now.type == pygame.constants.MOUSEBUTTONDOWN and self.player.whatihave['weapontree'] is True:
                self.weapontree.rect.center = self.player.rect.center
                self.player.whatihave['weapontree'] = False
                self.weapontree.flytree = True
                self.weapontree.clickpos = e_now.pos
            if e_now.type == pygame.constants.KEYDOWN and e_now.key == pygame.constants.K_SPACE:
                self.light = sprites.Light(0,0,'rect', BLUE,[WEIDTH,HIGHT],self)
                self.group.append(self.light)
            if self.ivlnpc.attack is False:
                if e_now.type == self.test_event:
                    self.ivlnpc.attack = True
                
            if e_now.type == pygame.constants.QUIT:
                stop = -1
            else:
                stop = 1
        
        return stop
    def update(self):
        pygame.display.set_caption(f"{int(self.fps.get_fps())}")
        self.player.update()
        self.camera.spy(self.player)
        self.npc.update(self.player.rect)
        self.ivlnpc.update()
        self.neprozrach()
        self.weapontree.update()
        self.group.update()
        pygame.display.update()


    def draw(self):
        self.surface.fill((0,0,0))
        for plitka in self.mapp.plitochnikkid:
            plitka.draw(self.surface, self.camera.newrectsprite(plitka.rect))

        self.npc.draw(self.surface,self.camera.newrectsprite(self.npc.rect))
        self.ivlnpc.draw(self.surface,self.camera.newrectsprite(self.ivlnpc.rect))
        self.weapontree.draw(self.surface)
        self.player.draw(self.surface, self.camera.newrectsprite(self.player.rect))
        self.group.draw(self.surface)
    def run(self):
        stop = 1
        self.new()
        while stop > 0:
            stop = self.events()
            self.draw()
            self.update()
            self.tick = self.fps.tick(60)
            

game = Game(WEIDTH, HIGHT, "playerpng.png", "map2.csv", 'mapstaff.png')
game.run()