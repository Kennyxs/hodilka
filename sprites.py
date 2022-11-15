import pygame
import dop


class Clasprite(pygame.sprite.Sprite):
    def __init__(self,image, place_x = 0, place_y = 0, ):
        self.vector = pygame.math.Vector2()
        self.image = image
        self.player = dop.imagecuter(image = image)
        self.delitelb = self.player.imager()     
        self.rect = self.delitelb.get_rect()

    def draw(self, surface):
        surface.blit(self.delitelb, self.rect)

    def update(self):
        press = pygame.key.get_pressed()
        if press[pygame.K_UP] is True:
            self.vector.y = -1
        if press[pygame.K_DOWN] is True:
            self.vector.y = 1
        self.rect.y += self.vector.y