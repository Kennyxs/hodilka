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
                img = Plitka(self.imlist[int(imagenow)], y, x)
                plitochka.append(img)
                x += imageweidth
            y +=imageweidth
            x = 0
        return plitochka
    def drawplitochnik(self,surface,newrect):
        for t in self.plitochnikkid:
            t.draw(surface,newrect)



class Plitka:
    def __init__(self, plitaimg, y, x) -> None:
        self.plitaimg = plitaimg
        self.rect = plitaimg.get_rect(topleft = (x, y))
    def draw(self,surface,newrect):
        surface.blit(self.plitaimg, newrect)





class Camera:
    def __init__(self):
        self.move = (0, 0)

    def spy(self, player):
        x = - player.rect.x + WEIDTH//2
        y = - player.rect.y + HIGHT//2
        if x < 0:
            x = 0
        if x> WEIDTH//2:
            x = 0
        if y<0:
            y = 0
        if y> HIGHT//2:
            y = 0
        
        self.move = (x,y)

    def newrectsprite(self,spriterect):
       return spriterect.move(self.move)
       
    