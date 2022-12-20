import pygame
import dop


class Clasprite(pygame.sprite.Sprite):
    def __init__(self,image, game, place_x = 0, place_y = 0):
        self.vector = pygame.math.Vector2()
        self.image = image
        self.player = dop.imagecuter(image = image)
        self.delitelb = self.player.imager()  
        self.delitelkartinok()   
        self.rect = self.delitelb.get_rect()
        self.skolko = len(self.listt_d)
        self.frame = 0
        self.secanimation = 0
        self.game =  game
        self.littlerect = pygame.rect.Rect(self.rect.x+12 ,self.rect.y +18, self.rect.width//4, self.rect.height//4)

        
    def draw(self, surface, certainrect):
        surface.blit(self.delitelb, certainrect)
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
        if self.wallwalker(self.game.spritemaplist):
            self.vector.update(0,0)
        
        self.rect.y += self.vector.y
        self.rect.x += self.vector.x
        self.littlerect.y += self.vector.y
        self.littlerect.x += self.vector.x
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
        sec = pygame.time.get_ticks()
        
        if self.vector.length() > 0  and sec - self.secanimation >= 500:
            self.secanimation = pygame.time.get_ticks()
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
            
    def wallwalker(self, spritemaplist):
        mover = self.littlerect.move((self.vector.x, self.vector.y))
        for t in spritemaplist:
            if mover.colliderect(t.rect) and t.boolean is True:
                return True
        return False
    

class NPC:
    def __init__(self,x,y,image) -> None:
        self.coordx = x
        self.coordy = y
        self.img = image
        self.rect = image.get_rect(x = self.coordx, y = self.coordy)
    def draw(self,surface,camera):
        surface.blit(self.img, camera)

class Speaker(NPC):
    def __init__(self, x, y, image,speakwindow,speed) -> None:
        self.speakwindow = speakwindow
        self.speed = speed
        super().__init__(x, y, image)
    def update(self):
        self.rect.x +=self.speed
        if abs(self.coordx - self.rect.x) >100:
            self.speed = -self.speed


    