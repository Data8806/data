'''分数'''
import pygame
class GameScore(pygame.sprite.Sprite):
    def __init__(self,score):
        super().__init__()
        self.font = pygame.font.SysFont("宋体",60)
        self.create_image(score)

    def create_image(self,score):
        text = f"{str(score)} floors"
        # text = str(score)
        self.image = self.font.render(text, True, (255,255,255))
        self.rect = self.image.get_rect()
        self.rect.left = 300
        self.rect.top = 20 
        