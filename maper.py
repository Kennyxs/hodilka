from settings import *
import dop

class Map:
    def __init__(self, mapfile, imagefile) -> None:
        self.mapfile = mapfile
        self.imagefile = imagefile
        self.list = self.csvv()
        self.imlist = self.imager()
    def csvv(self):
        file = open (self.mapfile)
        mlist = []
        for t in file:
            t = t[0 :-1]
            mlist.append(t.split(","))
        file.close()
        return mlist
    def imager(self):
        image = dop.imagecuter(self.imagefile)
        sizew = self.imagefile.get_width()
        sizeh= self.imagefile. get_height()
        imlist = []
        x = 0
        y = 0
        for d in range (sizeh//IMAGESIZE):
            for t in range (sizew//IMAGESIZE) :
                imlist.append(image.imager(wherex = x, wherey = y, weidth= IMAGESIZE, height= IMAGESIZE))
                x += IMAGESIZE
            y += IMAGESIZE
            x = 0
        return imlist
    def plitochnik(self):
        x =0
        y = 0
        plitochka = []
        for t in self.imlist:
            img = Plitka(t, 0, 0)
            plitochka.append(img)
            



class Plitka:
    def __init__(self, plitaimg, y, x) -> None:
        self.plitaimg = plitaimg
        self.rect = plitaimg.get_rect(topleft = (x, y))
    def draw(self,surface):
        surface.blit(self.plitaimg, self.rect)
