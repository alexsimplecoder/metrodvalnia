import pygame, random
from scripts import utils, camera, settings

pygame.init()

class Falling_Spikes:
    def __init__(self, coords):
        self.x, self.y = coords
        self.random_image = random.randint(0, 1)
        self.state = "hanging"
        self.speed = 0
        if self.random_image == 0:
            self.image = utils.load_image("assets/platformer_metroidvania asset pack v1.01/miscellaneous sprites/spikes.png", 1)
        else:
            self.image = utils.load_image("assets/platformer_metroidvania asset pack v1.01/miscellaneous sprites/spikes_trap.png", 1)
    def render(self, screen:pygame.Surface):
        screen.blit(self.image, (self.x - camera.camerax, self.y - camera.cameray))
    def update(self):
        if self.state == "hanging":
            pass
        else:
            self.speed += settings.gravity
            self.y += self.speed