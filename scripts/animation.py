import pygame
from scripts import utils

class Animation:
    def __init__(self, path:str, scale:float, image_num:int):
        self.images = utils.load_images(path, scale, image_num)
        self.index = 0
        
    def render(self, screen:pygame.Surface, coords:list[float, float]):
        screen.blit(self.images[self.index], coords)

    def update(self):
        if self.index < len(self.images) - 1:
            self.index += 1
        else:
            self.index = 0