import pygame

from scripts import animation, settings

pygame.init()

class Before_Jump_Dust:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.anim = animation.Animation(
            "assets/platformer_metroidvania asset pack v1.01/herochar sprites(new)/herochar_before_jump_dust_anim_strip_4.png",
            settings.dust_scale,
            4,
            0.17,
            repeatable=False
        )

    def render(self, screen:pygame.Surface):
        self.anim.render(screen, (self.x, self.y), "right")

    def update(self):
        self.anim.update()


class After_Jump_Dust(Before_Jump_Dust):
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.anim = animation.Animation(
            "assets/platformer_metroidvania asset pack v1.01/herochar sprites(new)/herochar_after_jump_dust_anim_strip_4.png",
            settings.dust_scale,
            4,
            0.17,
            repeatable=False
        )
dust_particles:list[Before_Jump_Dust | After_Jump_Dust] = []