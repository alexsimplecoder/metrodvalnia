import pygame, pytmx
from scripts import animation, settings, camera

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
        self.anims[self.state].render(screen, (self.x - camera.camerax, self.y - camera.cameray if self.state == "spinning" else self.y - camera.cameray - self.anims["spinning"].images[0].get_height()), "right")
        # pygame.draw.rect(screen, (255, 0, 0), self.get_hitbox().move(-camera.camerax, -camera.cameray), 2)

    def update(self, player):
        self.anims[self.state].update()
        if self.state == "collected":
            if self.anims[self.state].finished:
                items.remove(self)
                player.coins += 1

    def get_hitbox(self):
        hitbox = pygame.Rect(self.x, self.y, self.anims[self.state].images[0].get_width(), self.anims[self.state].images[0].get_height())
        return hitbox

items = []

def load_items():
    world = pytmx.load_pygame("tiled/world.tmx")
    for (xt, yt, tile_id) in world.get_layer_by_name("coins"):
        if tile_id != 0:
            items.append(Coin((xt * settings.tile_size, yt * settings.tile_size)))