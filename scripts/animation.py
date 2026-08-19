import pygame
from scripts import utils, settings

class Animation:
    def __init__(self, path:str, scale:float, image_num:int, anim_speed_insec:float):
        self.images = utils.load_images(path, scale, image_num)
        self.index = 0
        self.index2 = 0
        self.speed = anim_speed_insec
        
    def render(self, screen:pygame.Surface, coords:list[float, float] | tuple[float, float]):
        screen.blit(self.images[self.index], coords)

    def update(self):
        if self.index2 >= self.speed * settings.FPS:
            if self.index < len(self.images) - 1:
                self.index += 1
            else:
                self.index = 0
            self.index2 = 0
        self.index2 += 1