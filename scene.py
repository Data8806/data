import pygame, sys
from gameresource import *
from constants import *
from pygame.locals import*

class Scene:
    def update(self, window): pass
    def draw(self, window): pass
    def handle_events(self, window, events): pass


class Menu_Scene(Scene):   #开始界面
    def __init__(self):
        self.image1 = start_imgae
        self.rect1 = self.image1.get_rect()
        self.rect2 = Rect(229,176,84,76)

    def draw(self,window):
        window.canvas.blit(self.image1,(0,0))

    def handle_events(self, window, events):
        for en in events:
            if en.type == pygame.MOUSEBUTTONUP:
                if self.rect2.collidepoint(en.pos):
                    window.active_scene = game_scene

    

class Game_Scene(Scene):   #游戏界面
    def update(self,window):
        window.server.update()

    def draw(self,window):
        window.canvas.fill(Color(161,216,230))
        window.canvas.blit(bg_image,(15,80))
        window.canvas.blit(side_image,(0,80))
        window.canvas.blit(side_image,(495,80))
        window.canvas.blit(side_image,(0,441))
        window.canvas.blit(side_image,(495,441))
        window.server.draw(window.canvas)

    def handle_events(self,window,events):
            if window.server.game_over == True:
                window.active_scene = ending_scene

            window.server.handle_keys()
            for en in events:
                if en.type == pygame.KEYDOWN and en.key == pygame.K_p:
                    window.active_scene = pause_scene

class Pause_Scene(Scene):  #暂停界面
    def __init__(self):
        self.image = pause_image

    def draw(self,window):
        window.canvas.blit(self.image,(0,0))

    def handle_events(self,window,events):
        for en in events:
            if en.type == pygame.KEYDOWN and en.key == pygame.K_p:
                window.active_scene = game_scene



class Ending_Scene(Scene):  #结束界面
    def __init__(self):
        self.image = over_image
        
    def draw(self,window):
        window.canvas.blit(self.image,(0,0))

    def handle_events(self,window,events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_n:
                    window.server.restart()
                    window.active_scene = game_scene
                if e.key == pygame.K_r:
                    window.server.restart()
                    window.active_scene = start_scene


game_scene = Game_Scene()

start_scene = Menu_Scene()

pause_scene = Pause_Scene()

ending_scene = Ending_Scene()