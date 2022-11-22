import pygame
import dop


class Clasprite(pygame.sprite.Sprite):
    def __init__(self,image, place_x = 0, place_y = 0, ):
        self.vector = pygame.math.Vector2()
        self.image = image
        self.player = dop.imagecuter(image = image)
        self.delitelb = self.player.imager()  
        self.delitelkartinok()   
        self.rect = self.delitelb.get_rect()
        self.skolko = len(self.listt_d)
        self.frame = 0
        

        
    def draw(self, surface):
        surface.blit(self.delitelb, self.rect)

    def update(self):
        press = pygame.key.get_pressed()
        self.vector.update(0,0)
        if press[pygame.K_UP] is True:
            self.vector.y = -1
        if press[pygame.K_DOWN] is True:
            self.vector.y = 1
        if press[pygame.K_LEFT] is True:
            self.vector.x = -1
        if press[pygame.K_RIGHT] is True:
            self.vector.x = 1
        # if self.vector.length() > 0:
        #     pass
        self.rect.y += self.vector.y
        self.rect.x += self.vector.x
        self.animation()

        
    def delitelkartinok(self):
        self.listt_d = []
        self.listt_l =[]
        self.listt_r = []
        self.listt_u = []
        li = [self.listt_d,self.listt_l,self.listt_r,self.listt_u]
        y =0
        x = 0
        for t in li:
            for lister in range(4):
                t.append(self.player.imager(wherey = y, wherex = x))
                x +=32
            y+=32
            x = 0
    
    def animation(self):
        print(pygame.time.get_ticks())
        if self.vector.length() > 0  :
            num = []
            if self.vector.y >0:
                num = self.listt_d
            if self.vector.y < 0:
                num = self.listt_u
            if self.vector.x > 0:
                num = self.listt_r
            if self.vector.x < 0:
                num = self.listt_l
            if self.frame < self.skolko:
                self.delitelb = num[self.frame]
                self.frame +=1
            else:
                self.frame = 0