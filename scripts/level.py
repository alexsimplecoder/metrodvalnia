import pygame
import pytmx
from scripts import utils, settings

hard_blocks:dict[tuple[int, int], pygame.Rect] = {

}
world = None
map = None

def render(screen:pygame.Surface):
    screen.blit(world, (0, 0))
    for i in hard_blocks.values():
        pygame.draw.rect(screen, (255, 0, 0), i, 1)

def load_level():
    global world, map
    map = pytmx.load_pygame("tiled/world.tmx")
    world = utils.load_image("tiled/world.png", settings.level_scale)
    for x, y, gid in map.get_layer_by_name("ground"):
        if gid != 0:
            hard_blocks[(x, y)] = pygame.Rect((x * settings.tile_size, y * settings.tile_size, settings.tile_size, settings.tile_size))