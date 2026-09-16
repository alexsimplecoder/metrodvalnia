import pygame
from scripts import settings, player, keybinding, level, particle, enemies

pygame.init()

info = pygame.display.Info()

screen_width = info.current_w
screen_height = info.current_h

screen = pygame.display.set_mode((screen_width, screen_height))

level.load_level()

main_player = player.Player((500, 500))
enemies.load_enemies()
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
                main_player.jump()
            if i.key == keybinding.attack:
                main_player.state = "attack"
        if i.type == pygame.KEYUP:
            if i.key == keybinding.left:
                main_player.ml = False
            if i.key == keybinding.right:
                main_player.mr = False
    level.render(screen)
    for dust in particle.dust_particles:
        dust.render(screen)
        dust.update()
        if dust.anim.finished:
            particle.dust_particles.remove(dust)
    for enemy in enemies.enemies:
        enemy.render(screen)
        enemy.update()
    main_player.render(screen)
    main_player.update()
    pygame.display.update()