'''游戏中介模块'''
import pygame

from enemy import*

from hp import HP

from player import Plane
import time

from score import GameScore
import random
class GameServer:
    def __init__(self):
        self.restart()

    def restart(self):
        self.deep = 720
        self.game_over = False
        self.now = None
        self.number = -1

        self.is_pause = False

        self.all_sprites = pygame.sprite.Group()    # 游戏所有精灵组，负责更新与绘制
        self.en = pygame.sprite.Group()  #敌机精灵组

        self.top = Top()
        self.top.add(self.all_sprites, self.en)

        self.player = Plane()
        self.all_sprites.add(self.player)

        self.A = A(65,620)
        self.A.add(self.all_sprites,self.en)
        self.hp = HP(self.player.blood)
        self.all_sprites.add(self.hp)

        self.score = GameScore(self.number)
        self.all_sprites.add(self.score)


        self.create_last = pygame.time.get_ticks()
        self.create_delay = 600

    def update(self):
        self.all_sprites.update()
        self.check_collision()
        self.come_enemys()
        self.over_game()

    def draw(self, screen):
        self.all_sprites.draw(screen)

    def handle_keys(self):   #处理键盘事件
        keys = pygame.key.get_pressed()   #获取按键
        self.player.control(keys)

    def check_collision(self):
        self.hit_enemys()

    def hit_enemys(self):
        i = pygame.sprite.spritecollideany(self.player,self.en)
        if i == None:
            self.player.yoffset = 5
        else:
            if self.now != i:
                self.number += 1
                self.score.kill()
                self.score = GameScore(self.number)
                self.all_sprites.add(self.score)
                self.player.yoffset = i.yoffset

                if i.id == 0:
                    B_mixer.play()
                    self.player.blood -= 30
                    self.hp = HP(self.player.blood)
                    self.all_sprites.add(self.hp)

                elif i.id == 1:
                    A_mixer.play()
                    self.player.blood += 10
                    self.hp = HP(self.player.blood)
                    self.all_sprites.add(self.hp)
                    self.now = i

                elif i.id == 2:
                    B_mixer.play()
                    self.player.blood -= 30
                    self.hp = HP(self.player.blood)
                    self.all_sprites.add(self.hp)
                    self.now = i

                elif i.id == 4:
                    self.player.xoffset -= 4
                    print(self.player.xoffset)
                    self.now = i          
            
    def come_enemys(self):
        now = pygame.time.get_ticks()
        if now - self.create_last > self.create_delay:
            self.create_last = now
            self.en_list = ["A","B","D"]
            number = random.randint(0,2)
            en = eval(self.en_list[number])(random.randrange(65,425),self.deep)           
            en.add(self.all_sprites,self.en)

    def over_game(self):
        if self.player.blood <= 0 or self.player.rect.bottom >= GAME_HEIGHT:
            self.game_over = True
            dead_mixer.play()


