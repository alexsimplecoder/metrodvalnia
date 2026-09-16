import pygame

from scripts import level, settings, particle

from abc import ABC, abstractmethod

class Physics_Entity(ABC):
    def __init__(self, coords, moving_speed, jump_power):
        self.x, self.y = coords
        self.moving_speed = moving_speed
        self.jump_power = jump_power
        self.mr = False
        self.ml = False
        self.vy = 0
        self.dir = "left"
        self.state = "idle"
        self.max_jumps = 2
        self.jumps_left = self.max_jumps
        self.time_in_the_air = 0

    @abstractmethod
    def render(self, screen):
        pass

    def update(self):
        if self.ml == True and self.mr == False:
            self.x -= self.moving_speed
            self.state = "walk"
            self.dir = "left"
            self.collision_x()
        if self.mr == True and self.ml == False:
            self.x += self.moving_speed
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

    def jump(self):
        if self.jumps_left > 0:
            self.jumps_left -= 1
            self.vy = -self.jump_power
            if self.time_in_the_air < 5:
                particle.dust_particles.append(particle.Before_Jump_Dust((self.get_hitbox().left - 12, self.get_hitbox().centery - 25)))

    @abstractmethod
    def get_hitbox(self):
        pass

    @abstractmethod
    def calibration_x(self, hitbox):
        pass

    @abstractmethod
    def calibration_y(self, hitbox):
        pass

    def collision_x(self):
        hitbox = self.get_hitbox()
        player_tiles = level.get_collisions(hitbox)
        for i in player_tiles:
            if hitbox.colliderect(i):
                if self.mr == True:
                    hitbox.right = i.left
                else:
                    hitbox.left = i.right
        self.calibration_x(hitbox)

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
        self.calibration_y(hitbox)