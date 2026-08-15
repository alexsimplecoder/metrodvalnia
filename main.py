import pygame
from scripts import settings, utils, animation

pygame.init()

info = pygame.display.Info()

screen_width = info.current_w
screen_height = info.current_h

anim = animation.Animation("assets/platformer_metroidvania asset pack v1.01/herochar sprites(new)/herochar_attack_anim_strip_4(new).png", 5, 4)

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
while True:
    clock.tick(settings.FPS)
    screen.fill((255, 255, 255))
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    anim.render(screen, (50, 50))
    anim.update()
    pygame.display.update()