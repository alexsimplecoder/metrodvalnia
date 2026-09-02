import pygame
from scripts import animation, settings, level, particle

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
        self.w = self.anims["idle"].images[0].get_width()
        self.h = self.anims["idle"].images[0].get_height()
        self.state = "idle"
        self.dir = "right"
        self.mr = False
        self.ml = False
        self.vy = 0
        self.max_jumps = 2
        self.jumps_left = self.max_jumps
        self.time_in_the_air = 0

    def render(self, screen:pygame.Surface):
        self.anims[self.state].render(screen, (self.x, self.y), self.dir)
        hitbox = self.get_hitbox()

    def update(self):
        self.anims[self.state].update()
        if self.ml == True and self.mr == False:
            self.x -= 3
            self.state = "walk"
            self.dir = "left"
            self.collision_x()
        if self.mr == True and self.ml == False:
            self.x += 3
            self.state = "walk"
            self.dir = "right"
            self.collision_x()
        if self.ml == self.mr == False:
            self.state = "idle"
        if self.ml == self.mr == True:
            self.state = "idle"
        if self.vy < 0:
            self.time_in_the_air += 1
            if self.time_in_the_air > 5:
                self.state = "jump up"
        if self.vy > 0:
            self.time_in_the_air += 1
            if self.time_in_the_air > 5:
                self.state = "jump down"
        if self.max_jumps == 2 and self.jumps_left == 0:
            self.state = "double jump"
        self.vy += settings.gravity
        self.y += self.vy
        self.collision_y()

    def get_hitbox(self):
        return pygame.Rect(self.x, self.y, self.w, self.h).inflate(-38, -8)

    def collision_x(self):
        hitbox = self.get_hitbox()
        player_tiles = level.get_collisions(hitbox)
        for i in player_tiles:
            if hitbox.colliderect(i):
                if self.mr == True:
                    hitbox.right = i.left
                else:
                    hitbox.left = i.right
        self.x = hitbox.left - 19
    def collision_y(self):
        hitbox = self.get_hitbox()
        player_tiles = level.get_collisions(hitbox)
        for i in player_tiles:
            if hitbox.colliderect(i):
                if self.vy >= 0:
                    # when falling
                    hitbox.bottom = i.top
                    self.vy = 0
                    self.jumps_left = self.max_jumps
                    if self.time_in_the_air > 5:
                        particle.dust_particles.append(particle.After_Jump_Dust((self.get_hitbox().left - 12, self.get_hitbox().centery - 25)))
                    self.time_in_the_air = 0
                else:
                    # hitting from the bottom
                    hitbox.top = i.bottom
                    self.vy = 0
        self.y = hitbox.top - 4