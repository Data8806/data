'''游戏主界面'''

import pygame,sys

from pygame.locals import*

from constants import*

from gameresource import*

from gameserver import GameServer

from scene import*


class MainFrame:
    def __init__(self):
        pygame.display.set_caption(GAME_NAME)
        self.canvas = pygame.display.set_mode((GAME_WIDTH,GAME_HEIGHT))
        self.clock = pygame.time.Clock()
        self.server = GameServer()
        self.active_scene = start_scene


    def main_loop(self):
        while True:
            self.clock.tick(GAME_FPS)
            es = pygame.event.get()
            for events in es:
                if events.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    return
            self.active_scene.handle_events(self,es)
            self.active_scene.update(self)
            self.active_scene.draw(self)
            pygame.display.flip()
