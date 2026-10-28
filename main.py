import pygame
from scripts import settings, player, keybinding, level, particle, enemies, camera, item

pygame.init()

info = pygame.display.Info()

screen_width = info.current_w
screen_height = info.current_h

screen = pygame.display.set_mode((screen_width, screen_height))

settings.screen_w = screen_width
settings.screen_h = screen_height

level.load_level()
item.load_items()

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
            if i.key == keybinding.jump and main_player.state != "hit":
                main_player.jump()
            if i.key == keybinding.attack:
                if main_player.state != "attack" and main_player.state != "hit":
                    for enemy in enemies.enemies:
                        enemy.took_damage = False
                    main_player.attack_timer = 0
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
        enemy.update(main_player)
    main_player.render(screen)
    main_player.update()
    for i in item.items:
        i.render(screen)
        i.update(main_player)
        if main_player.get_hitbox().colliderect(i.get_hitbox()):
            i.state = "collected"
    camera.track((main_player.x, main_player.y))
    pygame.display.update()