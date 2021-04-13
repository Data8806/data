'''游戏入口'''

import pygame,os

from mainwindow import MainFrame

pygame.init()    #初始化pygame模块

os.environ['SDL_VIDEO_CENTERED'] = '1'    #窗口居中
  
frame = MainFrame()

pygame.mixer.music.play(loops = -1)

frame.main_loop()

pygame.mixer.music.stop()