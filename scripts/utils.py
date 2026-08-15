import pygame
from scripts import image_loader
pygame.init()

def load_image(path:str, scale:float)->pygame.Surface:
    image = image_loader.get_image(path)
    return pygame.transform.scale_by(image, scale)

def load_images(path:str, scale:float, image_num:int)->list[pygame.Surface]:
    sprites = []
    image = load_image(path, scale)
    w = image.get_width()/image_num
    h = image.get_height()
    for i in range(image_num):
        sprites.append(image.subsurface((i * w, 0, w, h)))
    return sprites