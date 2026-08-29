import pygame
from scripts import settings, player, keybinding, level

pygame.init()

info = pygame.display.Info()

screen_width = info.current_w
screen_height = info.current_h

screen = pygame.display.set_mode((screen_width, screen_height))

level.load_level()

main_player = player.Player((500, 500))
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
            if i.key == keybinding.left:
                main_player.ml = True
            if i.key == keybinding.right:
                main_player.mr = True
            if i.key == keybinding.jump:
                if main_player.jumps_left > 0:
                    main_player.vy = -7
                    main_player.jumps_left -= 1
        if i.type == pygame.KEYUP:
            if i.key == keybinding.left:
                main_player.ml = False
            if i.key == keybinding.right:
                main_player.mr = False
    level.render(screen)
    main_player.render(screen)
    main_player.update()
    pygame.display.update()