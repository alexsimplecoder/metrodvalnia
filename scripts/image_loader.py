import pygame

pygame.init()

cache = {

}

def get_image(path:str) -> pygame.Surface:
    if path in cache:
        return cache[path]
    else:
        cache[path] = pygame.image.load(path).convert_alpha()
    return cache[path]