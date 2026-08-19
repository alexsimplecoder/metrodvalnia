import pygame
from scripts import settings, utils, animation, player

pygame.init()

info = pygame.display.Info()

screen_width = info.current_w
screen_height = info.current_h

screen = pygame.display.set_mode((screen_width, screen_height))

main_player = player.Player((50, 50))
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
    main_player.render(screen)
    main_player.update()
    pygame.display.update()