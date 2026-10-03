import pygame
from scripts import animation, settings, level, particle, entity, image_loader, enemies
from interfaces.damageable import Damagable

pygame.init()

class Player(entity.Physics_Entity, Damagable):
    def __init__(self, coords:list[float, float]):
        entity.Physics_Entity.__init__(self, coords, 3, 7)
        Damagable.__init__(self, 100, 4)
        self.anims:dict[str, animation.Animation] = {
            "idle": animation.Animation("assets/platformer_metroidvania asset pack v1.01/herochar sprites(new)/herochar_idle_anim_strip_4.png", settings.scale, 4, 0.13),
            "walk": animation.Animation("assets/platformer_metroidvania asset pack v1.01/herochar sprites(new)/herochar_run_anim_strip_6.png", settings.scale, 6, 0.058),
            "jump up": animation.Animation("assets/platformer_metroidvania asset pack v1.01/herochar sprites(new)/herochar_jump_up_anim_strip_3.png", settings.scale, 3, 0.08),
            "jump down": animation.Animation("assets/platformer_metroidvania asset pack v1.01/herochar sprites(new)/herochar_jump_down_anim_strip_3.png", settings.scale, 3, 0.08),
            "double jump": animation.Animation("assets/platformer_metroidvania asset pack v1.01/herochar sprites(new)/herochar_jump_double_anim_strip_3.png", settings.scale, 3, 0.08),
            "attack": animation.Animation("assets/platformer_metroidvania asset pack v1.01/herochar sprites(new)/herochar_sword_attack_anim_strip_4.png", settings.scale, 4, 0.08, repeatable=False)
        }
        self.w = self.anims["idle"].images[0].get_width()
        self.h = self.anims["idle"].images[0].get_height()
        self.damage = 30

    def render(self, screen:pygame.Surface):
        if self.state != "attack":
            self.anims[self.state].render(screen, (self.x, self.y), self.dir)
        elif self.dir == "left":
            self.anims[self.state].render(screen, (self.x - 80, self.y), self.dir)
        else:
            self.anims[self.state].render(screen, (self.x, self.y), self.dir)
        hitbox = self.get_hitbox()
        attack_hitbox = self.get_attack_hitbox()
        # pygame.draw.rect(screen, (255, 0, 0), hitbox, 2)
        # pygame.draw.rect(screen, (255, 0, 0), attack_hitbox, 2)
        self.render_hp(screen, (20, 28))

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
        for enemy in enemies.enemies:
            if self.get_attack_hitbox().colliderect(enemy.get_hitbox()) and enemy.took_damage == False:
                enemy.damaged(self.damage)
                enemy.took_damage = True
        self.collision_y()
        self.attack_timer += 1

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

    def get_attack_hitbox(self):
        return pygame.Rect(self.x + self.anims["idle"].images[0].get_width() if self.dir == "right" else self.x - self.anims["idle"].images[0].get_width(), self.y, (self.anims["attack"].images[0].get_width())/2, self.anims["idle"].images[0].get_height())