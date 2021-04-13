'''游戏资源'''

import pygame
from os import path
from constants import*

img_dir = path.join(path.dirname(__file__),"imgs")

def load_image(name):
    fullname = path.join(img_dir,name)
    try:
        img = pygame.image.load(fullname)
    except:
        raise ValueError("无法加载{fullname}")
    return img

def load_music(name):
    fullename = path.join(music_dir,name)
    try:
        music = pygame.mixer.Sound(fullname)
    except:
        raise ValueError("无法加载{fullname}")
    return music

bg_image = load_image("背景.png")

side_image = load_image("线.png")

stab_image = load_image("2.png")
stab_image = pygame.transform.scale(stab_image,(100,20))

top_image = load_image("顶.png")

top_image = pygame.transform.scale(top_image,(480,20))

player_image = load_image("player1.png")

player_image = pygame.transform.scale(player_image,(32,40))

sq_image = load_image("3.jpg")
sq_image = pygame.transform.scale(sq_image,(100,20))

right_image = []

left_image = []

for i in range(1,5):
    fliename = f"右{i}.png"
    right_image.append(load_image(fliename))

for i in range(1,5):
    fliename = f"左{i}.png"
    left_image.append(load_image(fliename))


start_imgae = load_image("开始.jpg")

start_imgae = pygame.transform.scale(start_imgae,(GAME_WIDTH,GAME_HEIGHT))

pause_image = pygame.transform.scale(load_image("暂停.jpg"),(GAME_WIDTH,GAME_HEIGHT))

over_image = pygame.transform.scale(load_image("结束.png"),(GAME_WIDTH,GAME_HEIGHT))

elevator_image = []

for i in range(1,3):
    fliename = f"左滑{i}.png"
    elevator_image.append(load_image(fliename))

leaf_image = []
for i in range(1,4):
    fliename = f"弹簧{i}.png"
    img = load_image(fliename)
    leaf_image.append(img)

music_dir = path.join(path.dirname(__file__), "wavs")
pygame.mixer.init()
pygame.mixer.music.load(path.join(music_dir, "victory.mp3"))
A_mixer = pygame.mixer.Sound(path.join(music_dir,"A.wav"))
B_mixer = pygame.mixer.Sound(path.join(music_dir,"B.wav"))

dead_mixer = pygame.mixer.Sound(path.join(music_dir,"dead.wav"))