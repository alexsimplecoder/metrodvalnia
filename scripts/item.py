import pygame
from scripts import animation, settings

pygame.init()

class Coin:
    def __init__(self, coords):
        self.x, self.y = coords
        self.picked = False
        self.anims = {
            "spinning": animation.Animation("assets/platformer_metroidvania asset pack v1.01/miscellaneous sprites/coin_anim_strip_6.png", settings.scale, 6, 0.3),
            "collected": animation.Animation("assets/platformer_metroidvania asset pack v1.01/miscellaneous sprites/coin_pickup_anim_strip_6.png", settings.scale, 6, 0.1, False)
        }
        self.state = "spinning"

    def render(self, screen):
        self.anims[self.state].render(screen, (self.x, self.y))

    def update(self):
        self.anims[self.state].update()