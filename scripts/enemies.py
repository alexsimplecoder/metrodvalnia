import pygame, random, pytmx
from scripts import animation, settings, entity, camera
from interfaces import damageable

pygame.init()

class Goblin(entity.Physics_Entity, damageable.Damagable):
    def __init__(self, coords):
        entity.Physics_Entity.__init__(self, coords, 3, 7)
        damageable.Damagable.__init__(self, 100, 1.7)
        self.x, self.y = coords
        self.anims = {
            "walk" : animation.Animation("assets/platformer_metroidvania asset pack v1.01/enemies sprites/goblin/goblin_run_anim_strip_6.png", settings.scale, 6, 1),
            "idle" : animation.Animation("assets/platformer_metroidvania asset pack v1.01/enemies sprites/goblin/goblin_idle_anim_strip_4.png", settings.scale, 4, 1),
            "attack" : animation.Animation("assets/platformer_metroidvania asset pack v1.01/enemies sprites/goblin/goblin_attack_anim_strip_4.png", settings.scale, 4, 0.1),
            "hit" : animation.Animation("assets/platformer_metroidvania asset pack v1.01/enemies sprites/goblin/goblin_hit_anim_strip_3.png", settings.scale, 3, 0.1),
            "death" : animation.Animation("assets/platformer_metroidvania asset pack v1.01/enemies sprites/goblin/goblin_death_anim_strip_6.png", settings.scale, 6, 0.1, False),
            "jump down": animation.Animation("assets/platformer_metroidvania asset pack v1.01/enemies sprites/goblin/goblin_idle_anim_strip_4.png", settings.scale, 4, 1)
        }
        self.damage = 30
        self.timer = random.randint(settings.FPS * 2, settings.FPS * 3)
        self.hit_timer = 0
        self.random_movement = 1
        self.took_damage = False
        self.death_timer = int(settings.FPS * self.anims["death"].speed * len(self.anims["death"].rimages))
        
    def render(self, screen:pygame.Surface):
        self.anims[self.state].render(screen, (self.x - camera.camerax, self.y - camera.cameray), self.dir)
        # pygame.draw.rect(screen, (255, 30, 160), self.get_hitbox(), 1)
        if self.health < self.max_health:
            damageable.Damagable.render_hp(self, screen, (self.x - camera.camerax, self.y - 30 - camera.cameray))
        # pygame.draw.rect(screen, (255, 0, 0), self.get_attack_hitbox(), 2)

    def normal_update(self):
        super().update()

    def attack_update(self, main_player):
        self.state = "attack"
        if main_player.state != "hit":
            main_player.damaged(self.damage)
        

    def update(self, main_player):
        self.anims[self.state].update()
        if self.get_attack_hitbox().colliderect(main_player.get_hitbox()):
            self.attack_update(main_player)
        else:
            self.normal_update()
        self.ai()
        if self.hit_timer:
            self.state = "hit"
            self.hit_timer -= 1
        if self.health <= 0:
            self.state = "death"
            self.ml = False
            self.mr = False
            self.death_timer -= 1
        if self.death_timer == 0:
            enemies.remove(self)
        
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
            self.random_movement = random.choices([1, 2, 3], [48, 26, 26])[0]
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

    def damaged(self, damage):
        self.health -= damage
        self.hit_timer = int(self.anims["hit"].speed * len(self.anims["hit"].rimages) * settings.FPS)
        if self.health < 0:
            self.health = 0

    def get_attack_hitbox(self):
        if self.dir == "right":
            attack_hitbox = pygame.Rect(self.x + self.anims["idle"].images[0].get_width(), self.y, self.anims["attack"].images[0].get_width() - self.anims["idle"].images[0].get_width(), 100)
        else:
            attack_hitbox = pygame.Rect(self.x - self.anims["attack"].images[0].get_width() + self.anims["idle"].images[0].get_width() + 20, self.y, self.anims["attack"].images[0].get_width() - self.anims["idle"].images[0].get_width(), 100)
        return attack_hitbox

enemies:list[Goblin] = []

def load_enemies():
    map = pytmx.load_pygame("tiled/world.tmx")
    for (xt, yt, tile_id) in map.get_layer_by_name("goblins"):
        if tile_id != 0:
            goblin = Goblin((xt * settings.tile_size, yt * settings.tile_size))
            enemies.append(goblin)