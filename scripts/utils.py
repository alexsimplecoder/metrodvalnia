import pygame

def load_image(path:str, scale:float)->pygame.Surface:
    image = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale_by(image, scale)