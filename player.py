'''玩家'''

import pygame

from gameresource import*

from pygame.locals import*

class Plane(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.blood = 100
        self.rect.left = 15
        self.rect.top =  570
        self.index = 0
        self.xoffset = 0
        self.yoffset = 5


    def control(self,keys):
        if keys[K_LEFT]:
            self.xoffset = -5
            self.image = left_image[0]

        elif keys[K_RIGHT]:
            self.xoffset = 5
            self.image = right_image[0]
        else:
            self.xoffset = 0
            self.image = player_image


    def update(self):
        self.rect.top += self.yoffset
        self.rect.left += self.xoffset
        
        if self.blood >= 100:
            self.blood = 100
        if self.blood<= 0:
            self.blood = 0    
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= 495:
            self.rect.right = 495
        
