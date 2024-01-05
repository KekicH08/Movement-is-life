import sys

import pygame

import start_end_screen
from level_selection import level_selection


#  обработка событий
def events(screen, player, running, size, music_pause, clock, level, input_box, f):
    for event in pygame.event.get():
        #  выход
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #  управление персонажем
        elif event.type == pygame.KEYDOWN and not input_box.active:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.mup = True
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.mdown = True
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.mright = True
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.mleft = True

            #  управление музыкой
            if event.key == pygame.K_i:
                pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.2)
            if event.key == pygame.K_k:
                pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.2)
            if event.key == pygame.K_m:
                pygame.mixer.music.set_volume(0)
            if event.key == pygame.K_p:
                music_pause = not music_pause
                if music_pause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            #  выход
            if event.key == pygame.K_ESCAPE:
                start_end_screen.end_screen()

        elif event.type == pygame.KEYUP and not input_box.active:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.mup = False
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.mdown = False
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.mright = False
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.mleft = False

        #  выбор уровня
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            level, f = level_selection(player, mouse_pos, f, level)

        #  ввод имени игрока
        if player.hp == 0 or not player.started:
            input_box.handle_event(event)

    #  отображение интерфейса до начала игры
    if player.hp == 0 or not player.started:
        input_box.update()
        input_box.draw(screen)
        player.name = input_box.text

        pygame.draw.rect(screen, 'red', (1000, 15, 105, 50), 5)
        f1 = pygame.font.Font(None, 45)
        text1 = f1.render('Level', 1, (200, 0, 0))
        screen.blit(text1, (1010, 30))

        pygame.draw.rect(screen, 'red', (1120, 15, 50, 50), 5)
        f2 = pygame.font.Font(None, 50)
        text2 = f2.render('1', 1, (200, 0, 0))
        screen.blit(text2, (1135, 25))

        pygame.draw.rect(screen, 'red', (1120, 75, 50, 50), 5)
        f3 = pygame.font.Font(None, 50)
        text3 = f3.render('2', 1, (200, 0, 0))
        screen.blit(text3, (1135, 85))

        pygame.draw.rect(screen, 'red', (1120, 135, 50, 50), 5)
        f4 = pygame.font.Font(None, 50)
        text4 = f4.render('3', 1, (200, 0, 0))
        screen.blit(text4, (1135, 145))

        pygame.draw.rect(screen, 'red', (790, 15, 195, 50), 5)
        f5 = pygame.font.Font(None, 50)
        text5 = f5.render('Your name', 1, (200, 0, 0))
        screen.blit(text5, (800, 25))

        pygame.draw.rect(screen, 'crimson', (790, 135, 240, 50), 5)
        f5 = pygame.font.Font(None, 50)
        text5 = f5.render('Leaderboard', 1, (200, 0, 0))
        screen.blit(text5, (800, 145))

    #  блокировка выхода игрока за экран
    player.update()
    if player.pos[0] > size[0]:
        player.pos[0] = size[0] - player.size // 2
    elif player.pos[1] > size[1]:
        player.pos[1] = size[1] - player.size // 2

    #  анимация мигания игрока после получения урона (кадры неуязвимости)
    if player.f_after_hit > player.safe_frames:
        pygame.draw.circle(screen, pygame.Color(player.color), player.pos, player.size)
    elif player.f_after_hit < player.safe_frames and player.f_after_hit % 10 == 0:
        pygame.draw.circle(screen, pygame.Color(255, 180, 180), player.pos, player.size)
    elif player.f_after_hit < player.safe_frames and player.f_after_hit % 5 == 0:
        pygame.draw.circle(screen, pygame.Color(255, 120, 120), player.pos, player.size)
    elif player.f_after_hit < player.safe_frames and player.f_after_hit % 2 == 0:
        pygame.draw.circle(screen, pygame.Color(255, 90, 90), player.pos, player.size)
    else:
        pygame.draw.circle(screen, pygame.Color(player.color), player.pos, player.size)

    return [running, music_pause, clock, level, f]
