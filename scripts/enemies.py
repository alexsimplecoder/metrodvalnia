import pygame, random, pytmx
from scripts import animation, settings, entity

pygame.init()

class Goblin(entity.Physics_Entity):
    def __init__(self, coords):
        super().__init__(coords, 4, 3)
        self.x, self.y = coords
        self.anims = {
            "walk" : animation.Animation("assets/platformer_metroidvania asset pack v1.01/enemies sprites/goblin/goblin_run_anim_strip_6.png", settings.scale, 6, 1),
            "idle" : animation.Animation("assets/platformer_metroidvania asset pack v1.01/enemies sprites/goblin/goblin_idle_anim_strip_4.png", settings.scale, 4, 1),
            "attack" : animation.Animation("assets/platformer_metroidvania asset pack v1.01/enemies sprites/goblin/goblin_attack_anim_strip_4.png", settings.scale, 4, 1, False),
            "hit" : animation.Animation("assets/platformer_metroidvania asset pack v1.01/enemies sprites/goblin/goblin_hit_anim_strip_3.png", settings.scale, 3, 1, False),
            "death" : animation.Animation("assets/platformer_metroidvania asset pack v1.01/enemies sprites/goblin/goblin_death_anim_strip_6.png", settings.scale, 6, 1, False),
            "jump down": animation.Animation("assets/platformer_metroidvania asset pack v1.01/enemies sprites/goblin/goblin_idle_anim_strip_4.png", settings.scale, 4, 1)
        }
        self.damage = 30
        self.health = 100
        self.timer = random.randint(settings.FPS * 2, settings.FPS * 3)
        self.random_movement = 1

    def render(self, screen:pygame.Surface):
        self.anims[self.state].render(screen, (self.x, self.y), self.dir)
        # pygame.draw.rect(screen, (255, 30, 160), self.get_hitbox(), 1)

    def normal_update(self):
        super().update()

    def attack_update(self):
        pass

    def update(self):
        self.anims[self.state].update()
        if self.state == "attack":
            self.attack_update()
        else:
            self.normal_update()
        self.ai()

    def get_hitbox(self):
        image = self.anims[self.state].images[0]
        hitbox = pygame.Rect(self.x, self.y, image.get_width(), image.get_height()).inflate(-30, 0)
        return hitbox

    def calibration_x(self, hitbox):
        self.x = hitbox.left - 15

    def calibration_y(self, hitbox):
        self.y = hitbox.top

    def ai(self):
        if self.timer == 0:
            self.random_movement = random.randint(1, 3)
            self.timer = random.randint(settings.FPS, int(settings.FPS * 1.5))
        if self.random_movement == 1:
            self.mr = False
            self.ml = False
        elif self.random_movement == 2:
            self.ml = False
            self.mr = True
        else:
            self.mr = False
            self.ml = True
        self.timer -= 1

enemies:list[Goblin] = []

def load_enemies():
    map = pytmx.load_pygame("tiled/world.tmx")
    for (xt, yt, tile_id) in map.get_layer_by_name("goblins"):
        if tile_id != 0:
            goblin = Goblin((xt * settings.tile_size, yt * settings.tile_size))
            enemies.append(goblin)