import pygame
from scripts import animation, settings

pygame.init()

class Player:
    def __init__(self, coords:list[float, float]):
        self.x = coords[0]
        self.y = coords[1]
        self.anims = {
            "idle": animation.Animation("assets/platformer_metroidvania asset pack v1.01/herochar sprites(new)/herochar_idle_anim_strip_4.png", settings.scale, 4, 0.13),
            "walk": animation.Animation("assets/platformer_metroidvania asset pack v1.01/herochar sprites(new)/herochar_run_anim_strip_6.png", settings.scale, 6, 0.058),
            "jump up": animation.Animation("assets/platformer_metroidvania asset pack v1.01/herochar sprites(new)/herochar_jump_up_anim_strip_3.png", settings.scale, 3, 0.08),
            "jump down": animation.Animation("assets/platformer_metroidvania asset pack v1.01/herochar sprites(new)/herochar_jump_down_anim_strip_3.png", settings.scale, 3, 0.08),
            "double jump": animation.Animation("assets/platformer_metroidvania asset pack v1.01/herochar sprites(new)/herochar_jump_double_anim_strip_3.png", settings.scale, 3, 0.08)
        }
        self.state = "idle"
        self.dir = "right"
        self.mr = False
        self.ml = False

    def render(self, screen:pygame.Surface):
        self.anims[self.state].render(screen, (self.x, self.y), self.dir)

    def update(self):
        self.anims[self.state].update()
        if self.ml == True and self.mr == False:
            self.x -= 3
            self.state = "walk"
            self.dir = "left"
        if self.mr == True and self.ml == False:
            self.x += 3
            self.state = "walk"
            self.dir = "right"
        if self.ml == self.mr == False:
            self.state = "idle"
        if self.ml == self.mr == True:
            self.state = "idle"