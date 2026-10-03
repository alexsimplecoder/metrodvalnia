from abc import ABC, abstractmethod
import pygame
from scripts import image_loader


class Damagable:
    def __init__(self, max_hpl, scale):
        self.max_health = max_hpl
        self.health = self.max_health
        self.image1 = image_loader.get_image("assets/platformer_metroidvania asset pack v1.01/hud elements/health_hud_left.png")
        self.image2 = image_loader.get_image("assets/platformer_metroidvania asset pack v1.01/hud elements/health_hud_middle.png")
        self.image3 = image_loader.get_image("assets/platformer_metroidvania asset pack v1.01/hud elements/health_hud_right.png") 
        self.image1 = pygame.transform.scale_by(self.image1, scale)
        self.image2 = pygame.transform.scale_by(self.image2, scale)
        self.image3 = pygame.transform.scale_by(self.image3, scale)
        self.w1 = self.image1.get_width() + self.image2.get_width() + self.image3.get_width()
        self.dy = self.image1.get_height() * 10/100

    def render_hp(self, screen:pygame.Surface, coords:tuple[float, float]):
        pygame.draw.rect(screen, (255, 0, 0), (coords[0], coords[1] + self.dy, self.w1, self.image1.get_height() - 2 * self.dy), border_radius=6)     
        pygame.draw.rect(screen, (0, 255, 0), (coords[0], coords[1] + self.dy,(self.health/self.max_health)*self.w1, self.image1.get_height() - 2 * self.dy), border_radius=6)
        screen.blit(self.image1, (coords[0], coords[1]))
        screen.blit(self.image2, (coords[0] + self.image1.get_width(), coords[1]))
        screen.blit(self.image3, (coords[0] + self.image1.get_width() + self.image2.get_width(), coords[1]))
        