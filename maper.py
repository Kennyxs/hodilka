from settings import *
import dop
import pygame

class Map:
    def __init__(self, mapfile, imagefile) -> None:
        self.newsizew = IMAGESIZE
        self.newsizeh = IMAGESIZE
        self.mapfile = mapfile
        self.imagefile = imagefile
        self.list = self.csvv()
        self.imageall  = pygame.image.load(self.imagefile)
        self.imlist = self.imager(16)
        self.plitochnikkid = self.plitochnik(self.newsizew)
        self.sizemapxe = len(self.list[0])*self.newsizew
        self.sizemapye = len(self.list)*self.newsizew
    
        
    def csvv(self):
        file = open (self.mapfile)
        mlist = []
        for t in file:
            t = t[0 :-1]
            mlist.append(t.split(","))
        file.close()
        return mlist
    def imager(self, hotimsizeimage):
        

        imagecut = dop.imagecuter(self.imageall)
        print(self.imageall)
        sizew = self.imageall.get_width()
        sizeh= self.imageall.get_height()
        if hotimsizeimage != IMAGESIZE:
            coeficent = hotimsizeimage-IMAGESIZE
            self.newsizew = IMAGESIZE + coeficent
            self.newsizeh = IMAGESIZE +  coeficent
            
            
        imlist = []
        x = 0
        y = 0
        for d in range (sizeh//IMAGESIZE):
            for t in range (sizew//IMAGESIZE) :
                
                cutimage = imagecut.imager(wherex = x, wherey = y, weidth=IMAGESIZE, height= IMAGESIZE)
                cutimage = pygame.transform.scale(cutimage, (self.newsizew, self.newsizeh))
                imlist.append(cutimage)
                x += IMAGESIZE
            y += IMAGESIZE
            x = 0
        return imlist
    def plitochnik(self, imageweidth):
        x =0
        y = 0
        plitochka = []
        for ryad in self.list:
            indeks = len(ryad)
            for stolbec in range(indeks):
                imagenow = ryad[stolbec]
                img = Plitka(self.imlist[int(imagenow)], y, x,int(imagenow))
                plitochka.append(img)
                x += imageweidth
            y +=imageweidth
            x = 0
        return plitochka
    def drawplitochnik(self,surface,newrect):
        for t in self.plitochnikkid:
            t.draw(surface,newrect)



class Plitka:
    def __init__(self, plitaimg, y, x, number) -> None:
        self.plitaimg = plitaimg
        self.rect = plitaimg.get_rect(topleft = (x, y))
        self.number = number
        self.boolean = True if number in WALL_IDS else False
        self.noprozrachno = 0
        
    def draw(self,surface,newrect):
        
        surface.blit(self.plitaimg, newrect)
        self.night = pygame.surface.Surface([self.rect.w,self.rect.h],pygame.SRCALPHA)
        self.night.fill((0,0,0,self.noprozrachno))
        surface.blit(self.night, newrect)





class Camera:
    def __init__(self, mapw,maph):
        self.move = (0, 0)
        self.mapw = mapw
        self.maph = maph

    def spy(self, player):
        dx = - player.rect.x + WEIDTH//2
        dy = - player.rect.y + HIGHT//2
        
        if dx < WEIDTH -  self.mapw:
            dx = WEIDTH -  self.mapw
        if dx > 0:
            dx = 0
        if dy<HIGHT - self.maph:
            dy = HIGHT - self.maph
        if dy> 0:
            dy = 0
        
        self.move = (dx,dy)

    def newrectsprite(self,spriterect):
       return spriterect.move(self.move)
       
    