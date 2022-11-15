import pygame 

class imagecuter:
    def __init__(self, image = None, way = None):
        if image != None:
            self.image = image
        elif way != None:
            self.image = pygame.image.load(way)
    def imager(self, wherey = 0, wherex = 0, weidth = 32, height = 32):
        surimage = self.image.subsurface(wherex, wherey, weidth, height)
        return surimage