from settings import *
import dop
import pygame

class Map:
    def __init__(self, mapfile, imagefile) -> None:
        self.mapfile = mapfile
        self.imagefile = imagefile
        self.list = self.csvv()
        self.imageall  = pygame.image.load(self.imagefile)
        self.imlist = self.imager()
        self.plitochnikkid = self.plitochnik(IMAGESIZE)
    def csvv(self):
        file = open (self.mapfile)
        mlist = []
        for t in file:
            t = t[0 :-1]
            mlist.append(t.split(","))
        file.close()
        return mlist
    def imager(self):
        imagecut = dop.imagecuter(self.imageall)
        print(self.imageall)
        sizew = self.imageall.get_width()
        sizeh= self.imageall.get_height()
        imlist = []
        x = 0
        y = 0
        for d in range (sizeh//IMAGESIZE):
            for t in range (sizew//IMAGESIZE) :
                imlist.append(imagecut.imager(wherex = x, wherey = y, weidth= IMAGESIZE, height= IMAGESIZE))
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
    def drawplitochnik(self,surface):
        for t in self.plitochnikkid:
            t.draw(surface)



class Plitka:
    def __init__(self, plitaimg, y, x) -> None:
        self.plitaimg = plitaimg
        self.rect = plitaimg.get_rect(topleft = (x, y))
    def draw(self,surface):
        surface.blit(self.plitaimg, self.rect)
