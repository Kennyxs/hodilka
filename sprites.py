import pygame
import dop
import pygame.freetype as free
import random 
from settings import*
import math


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
        self.whatihave = {'weaponsword' : False, 'weapontree' : False}
        self.speed = 0.07 
    def draw(self, surface, certainrect):
        surface.blit(self.delitelb, certainrect)
    def update(self):
        newspd = self.speed * self.game.tick
        press = pygame.key.get_pressed()
        self.vector.update(0,0)
        if press[pygame.K_UP] is True:
            self.vector.y = -(newspd)
        if press[pygame.K_DOWN] is True:
            self.vector.y = newspd
        if press[pygame.K_LEFT] is True:
            self.vector.x = -(newspd)
        if press[pygame.K_RIGHT] is True:
            self.vector.x = newspd
        if self.wallwalker(self.game.spritemaplist):
            self.vector.update(0,0)
        self.collidetree()
        self.rect.y += self.vector.y
        self.rect.x += self.vector.x
        self.littlerect.y += self.vector.y
        self.littlerect.x += self.vector.x
        self.animation()
        self.ghostzone()
        
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
        
        if self.vector.length() > 0  and sec - self.secanimation >= 200:
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
        if mover.colliderect(self.game.npc.rect):
            return True
        return False
    def collidetree(self):
        if self.rect.colliderect(self.game.weapontree.rect) and self.game.weapontree.flytree is False:
            self.whatihave ['weapontree' ] = True
    def ghostzone(self):
        if way(self.rect.center, self.game.ivlnpc.rect.center)<50:
            if abs(self.game.ivlnpc.coordx -self.game.ivlnpc.rect.x) <=100 and abs(self.game.ivlnpc.coordy -self.game.ivlnpc.rect.y) <=100:
                self.game.ivlnpc.zone = True
            else:
                self.game.ivlnpc.zone = False
        else:
            self.game.ivlnpc.zone = False

class NPC:
    def __init__(self,x,y,image) -> None:
        self.coordx = x
        self.coordy = y
        self.img = image
        self.rect = image.get_rect(x = self.coordx, y = self.coordy)

    def draw(self,surface,camera):
        surface.blit(self.img, camera)

class Speaker(NPC):
    def __init__(self, x, y, image,speakwindow,speed,game) -> None:
        self.speakwindow = speakwindow
        self.speed = speed
        self.dospeed = 0
        self.game = game
        super().__init__(x, y, image)
    def update(self,playerrect):
        if not self.rect.colliderect(playerrect) :
            self.rect.x +=self.speed
            Chat.nuler()            
        if abs(self.coordx - self.rect.x) >100:
            self.speed = -self.speed
        if self.rect.colliderect(playerrect):
            self.chat = Chat("hello",40,self.rect.x -10,self.rect.y -20,[255,255,255], self.game)
            self.chat.draw()
        
        
            

class Chat:
    ciferkadraw = 0

    def __init__(self,text,size,x,y,colour, game) -> None:
        self.text = text
        self.bukvi = ""
        self.size = size
        self.colour = colour
        self.rect =pygame.Rect(x,y,self.size,self.size//2)
        self.font = free.Font(None,10)
        self.fontsurface = pygame.Surface((self.size,self.size//2),pygame.SRCALPHA)
        self.game = game
        
        
    def draw(self):
        if Chat.ciferkadraw< len(self.text):
            self.bukvi = self.text[0 : int(Chat.ciferkadraw)]
        else:
            self.bukvi = self.text
        print(Chat.ciferkadraw)
        self.fontsurface.fill((0,0,0,50))
        self.font.render_to(self.fontsurface,(2,3),self.bukvi,self.colour)
        self.game.surface.blit(self.fontsurface, self.game.camera.newrectsprite(self.rect))
        Chat.ciferkadraw +=0.2
    @classmethod
    def nuler(cls):
        Chat.ciferkadraw = 0

class evilnpc(NPC):
    def __init__(self, x, y, image,game) -> None:
        self.game = game
        self.lives = 3
        self.times = 0

        self.speedx = 100
        self.speedy = 100
        self.wanish = 0
        self.zone = False
        self.speedall =   100
        self.attack = True
        self.lives = 3
        super().__init__(x, y, image)
    def draw(self,surface,camers):
        super().draw(surface,camers)
        self.ivlnight = pygame.Surface(self.img.get_size(), pygame.SRCALPHA)
        self.ivlnight.fill((0,0,0,self.wanish))
        surface.blit(self.ivlnight,camers)
    def update(self):
        tickspd = self.speedall * self.game.tick
        print(self.speedx, self.speedy)
        if self.attack is True:
            if self.zone is False:
                if pygame.time.get_ticks()-self.times>= 500:
                    self.speedx = math.ceil(random.randint(-100,100) * (self.game.tick/1000))
                    self.speedy = math.ceil(random.randint(-100,100) * (self.game.tick/1000))
                    
                    self.times = pygame.time.get_ticks()
                if abs(self.coordx -self.rect.x) >=100:
                    self.speedx =-math.ceil(self.speedx* (self.game.tick/1000))
                if abs(self.coordy - self.rect.y) >=100:
                    self.speedy = -math.ceil(self.speedy* (self.game.tick/1000))
            elif abs(self.coordx - self.rect.x) <100 and abs(self.coordy - self.rect.y) <100:
                
                x =  self.game.player.rect.center[0] - self.rect.center[0]
                y = self.game.player.rect.center[-1] - self.rect.center[-1]
                c = (x**2 + y**2)**0.5
                if y ==0 or x ==0:
                    sina = 0
                    cosa = 0
                else:
                    sina = y/c
                    cosa = x/c
                self.speedx = self.speedall*cosa
                self.speedy = self.speedall * sina
            else:
                self.zone = False 
                self.speedx,self.speedy = sinuser([self.coordx,self.coordy],[self.rect.centerx,self.rect.centery], self.speedall)
                self.speedx *=math.ceil(self.game.tick/1000)
                self.speedy *= math.ceil(self.game.tick/1000)
                
        else:
            self.speedx = 0
            self.speedy = 0 
            
        self.rect.x +=self.speedx
        self.rect.y += self.speedy
        self.collidetree()
    def collidetree(self):
        if self.rect.colliderect(self.game.weapontree.rect) and self.attack is True:
            light = Light(self.rect.x,self.rect.y,'rect', BLUE,self.rect.size,self.game)
            self.game.group.append(light)
            self.attack = False
            if self.game.weapontree.flytree is True:
                self.lives -= 1
                print(self.lives)
        
class Weapontree:
    def __init__(self, x,y,image,game):
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect(x = self.x, y = self.y)
        self.game = game
        self.speed = 10
        self.flytree = False
        self.clickpos = [0,0]

    def draw(self,surface):
        if self.game.player.whatihave['weapontree'] is False:
            surface.blit(self.image, self.game.camera.newrectsprite(self.rect))
    def update(self):
        rectandcamera = self.game.camera.newrectsprite(self.rect)
        if self.flytree is True:
            flyx = self.clickpos [0] - rectandcamera.center[0]  
            flyy = -(rectandcamera.center[-1] - self.clickpos [-1] )
            way  =((flyx *flyx) + (flyy*flyy) )**0.5
            try:
                sina = flyy/way 
                cosa = flyx/way
            except ZeroDivisionError:
                sina = flyy/1 
                cosa = flyx/1
            speedx = cosa *self.speed
            speedy = sina*self.speed
            if self.speed > 0:
                self.rect.x += speedx
                self.rect.y += speedy
                self.speed -= 1
            
            else:
                self.speed = 10
                self.flytree = False

class Light:
    def __init__(self,x,y,form,color,size, game) -> None:
        self.x = x
        self.y = y
        self.form = form
        self.color =list(color)
        self.size = size 
        self.wanish = 255
        self.game = game
        self.rect = pygame.rect.Rect([self.x,self.y],self.size )
        
        self.subsurf = pygame.surface.Surface(self.size, pygame.SRCALPHA)
        self.color.append(self.wanish) 
    def draw(self,surface):
       # print(self.color)
       # print ( f"const: {BLUE}")
       
        if self.form == "rect":
            self.subsurf.fill(self.color)
        if self.form == "elipse":
            
            pygame.draw.ellipse(self.subsurf,self.color,self.rect)
        newrect = self.game.camera.newrectsprite(self.rect)    
        surface.blit(self.subsurf,newrect)
    def update(self):
        if self.color[-1]>9:
            self.color[-1] -=10
        else:
            self.color[-1] = 0
        

class Group(list):
    def draw(self,surface):
        for t in self:
            t.draw(surface)
    def update(self):
        for t in self:
            t.update()
    



def sinuser(coordint , coordint2, speedall):
    x =  coordint[0] - coordint2[0]
    y = coordint[-1] - coordint2[-1]
    c = (x**2 + y**2)**0.5
    if y ==0 or x ==0:
        sina = 0
        cosa = 0
    else:
        sina = y/c
        cosa = x/c
    return [speedall*cosa, speedall * sina]

def way(coordint, coordint2):
    x = coordint[0] - coordint2[0]
    y = coordint[-1] - coordint2[-1]
    return  (x**2 + y**2)**0.5