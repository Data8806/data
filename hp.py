'''血条'''

import pygame

class HP(pygame.sprite.Sprite):
    def __init__(self, blood):
        super().__init__()
        self.create_image(blood)

    def create_image(self, blood):
        self.image = pygame.Surface((150,40))
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image,(255,0,0),(0,0,blood/100*self.rect.width,40),0)
        self.rect.topleft = (30,30)