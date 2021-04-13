'''敌人'''

from gameresource import*
import pygame
import random

class Top(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.id = 0
        self.yoffset = 5
        self.image = top_image
        self.rect = self.image.get_rect()
        self.create_image()

    def create_image(self):
        self.rect.left = 15
        self.rect.top = 80


class A(pygame.sprite.Sprite):
    def __init__(self,centerx,centery):
        super().__init__()
        self.id = 1
        self.image = sq_image
        self.rect = self.image.get_rect()
        self.rect.centery = centery
        self.rect.centerx = centerx
        self.yoffset = -3

    def update(self):
        self.rect.centery += self.yoffset
        if self.rect.top <= 80:
            self.kill()
        


class B(pygame.sprite.Sprite):
    def __init__(self,centerx,centery):
        super().__init__()
        self.id = 2
        self.image = stab_image
        self.rect = self.image.get_rect()
        self.rect.centery = centery
        self.rect.centerx = centerx
        self.yoffset = -3

    def update(self):
        self.rect.centery += self.yoffset
        if self.rect.top <= 80:
            self.kill()


class C(pygame.sprite.Sprite):
    def __init__(self,centerx,centery):
        super().__init__()
        self.id = 3
        self.index = 0
        self.image = leaf_image[self.index]
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.yoffset = -3
        self.animation_delay = 100        
        self.last_update = pygame.time.get_ticks()
        self.center = (self.rect.centerx,self.rect.centery)

    def update(self):
        self.rect.centery += self.yoffset
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_delay:
            self.last_update = now
            self.index += 1
            if self.index > 2:
                self.index = 0
            else:
                self.image = leaf_image[self.index]
                # self.rect = self.image.get_rect()
                # self.rect.center = self.center

        if self.rect.top <= 100:
            self.kill()


class D(pygame.sprite.Sprite):
    def __init__(self,centerx,centery):
        super().__init__()
        self.id = 4
        self.index = 0
        self.image = elevator_image[self.index]
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.yoffset = -3
        self.animation_delay = 100
        self.last_update = pygame.time.get_ticks()
        
    def update(self):
        self.rect.centery += self.yoffset
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_delay:
            self.last_update  = now 
            if self.index < 1:
                self.index += 1
            else:
                self.index = 0

            self.image = elevator_image[self.index]

        if self.rect.top <= 80:
            self.kill()




        


