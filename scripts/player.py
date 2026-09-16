import pygame
from scripts import animation, settings, level, particle, entity

pygame.init()

class Player(entity.Physics_Entity):
    def __init__(self, coords:list[float, float]):
        super().__init__(coords, 3, 7)
        self.anims = {
            "idle": animation.Animation("assets/platformer_metroidvania asset pack v1.01/herochar sprites(new)/herochar_idle_anim_strip_4.png", settings.scale, 4, 0.13),
            "walk": animation.Animation("assets/platformer_metroidvania asset pack v1.01/herochar sprites(new)/herochar_run_anim_strip_6.png", settings.scale, 6, 0.058),
            "jump up": animation.Animation("assets/platformer_metroidvania asset pack v1.01/herochar sprites(new)/herochar_jump_up_anim_strip_3.png", settings.scale, 3, 0.08),
            "jump down": animation.Animation("assets/platformer_metroidvania asset pack v1.01/herochar sprites(new)/herochar_jump_down_anim_strip_3.png", settings.scale, 3, 0.08),
            "double jump": animation.Animation("assets/platformer_metroidvania asset pack v1.01/herochar sprites(new)/herochar_jump_double_anim_strip_3.png", settings.scale, 3, 0.08),
            "attack": animation.Animation("assets/platformer_metroidvania asset pack v1.01/herochar sprites(new)/herochar_sword_attack_anim_strip_4.png", settings.scale, 4, 0.08, repeatable=False)
        }
        self.w = self.anims["idle"].images[0].get_width()
        self.h = self.anims["idle"].images[0].get_height()

    def render(self, screen:pygame.Surface):
        if self.state != "attack":
            self.anims[self.state].render(screen, (self.x, self.y), self.dir)
        elif self.dir == "left":
            self.anims[self.state].render(screen, (self.x - 80, self.y), self.dir)
        else:
            self.anims[self.state].render(screen, (self.x, self.y), self.dir)
        hitbox = self.get_hitbox()

    def calibration_x(self, hitbox):
        self.x = hitbox.left - 19

    def calibration_y(self, hitbox):
        self.y = hitbox.top - 4

    def attack_update(self):
        if self.anims["attack"].finished:
            self.state = "idle"
            self.anims["attack"].reset()
        if self.ml == True and self.mr == False:
            self.x -= 3
            self.dir = "left"
            self.collision_x()
        if self.mr == True and self.ml == False:
            self.x += 3
            self.dir = "right"
            self.collision_x()
        if self.vy < 0:
            self.time_in_the_air += 1
        if self.vy > 0:
            self.time_in_the_air += 1
        self.vy += settings.gravity
        self.y += self.vy
        self.collision_y()

    def normal_update(self):
        super().update()

    def update(self):
        self.anims[self.state].update()
        if self.state == "attack":
            self.attack_update()
        else:
            self.normal_update()

    def get_hitbox(self):
        return pygame.Rect(self.x, self.y, self.w, self.h).inflate(-38, -8)

    