import pygame
from scripts import utils, settings

class Animation:
    def __init__(self, path:str, scale:float, image_num:int, anim_speed_insec:float, repeatable:bool = True):
        self.images = utils.load_images(path, scale, image_num)
        self.index = 0
        self.time = 0
        self.speed = anim_speed_insec
        self.rimages = []
        for i in self.images:
            self.rimages.append(pygame.transform.flip(i, True, False))
        self.repeatable = repeatable
        self.finished = False
        
    def render(self, screen:pygame.Surface, coords:list[float, float] | tuple[float, float], dir:str):
        if dir == "right":
            screen.blit(self.images[self.index], coords)
        else:
            screen.blit(self.rimages[self.index], coords)

    def update(self):
        if self.time >= self.speed * settings.FPS:
            if self.index < len(self.images) - 1:
                self.index += 1
            else:
                if self.repeatable:
                    self.index = 0
                else:
                    self.index = len(self.images) - 1
                    self.finished = True
            self.time = 0
        self.time += 1

    def reset(self):
        self.index = 0
        self.time = 0
        self.finished = False