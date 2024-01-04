import pygame

import balls
import controls_interface
import movable_player
from balls_generation import generate_balls
from images import Heart, Sad_smile, all_sprites
from input_box import InputBox
from level_selection import leaderboard_refresh
from start_end_screen import start_screen


#  отображение количества здоровья игрока
def hearts_ind(player, screen):
    all_sprites.remove(all_sprites)
    if player.hp > 0:
        for i in range(1, player.hp + 1):
            Heart(i, player)
    else:
        Sad_smile()
    all_sprites.draw(screen)


def run():
    pygame.init()
    size = 1200, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Movement is life')
    bg_color = (235, 255, 255)

    fps = 60
    clock = pygame.time.Clock()
    running = True

    player = movable_player.Player([size[0] // 2, size[1] // 2])

    level = 1

    #  загрузка музыки для игры
    music = pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    music_pause = 1

    f = 0

    #  строка для ввода имени игрока
    input_box1 = InputBox(790, 75, 190, 50)

    #  цикл игры
    while running:
        f += 1

        #  генерация вражеских шариков
        if f % 7 == 0:
            if player.hp > 0:
                generate_balls(level)
            else:
                generate_balls(8)

        #  добавление очков за время
        if f % 60 == 0 and player.started and player.hp != 0:
            player.pts += 10

        #  отображения визуала
        screen.fill(bg_color)

        pts_font = pygame.font.Font(None, 100)
        pts_text = pts_font.render(str(player.pts), 1, (250, 200, 200))
        screen.blit(pts_text, (450, 15))

        hearts_ind(player, screen)
        balls.all_sprites.update(player, f)
        balls.all_sprites.draw(screen)

        #  обновление переменных
        running, music_pause, clock, level, f = controls_interface.events(screen, player, running, size, music_pause,
                                                                          clock, level, input_box1, f)

        #  запись результата в базу данных
        if player.hp == 0:
            leaderboard_refresh(player, level)

        pygame.display.flip()
        clock.tick(fps)


start_screen()
run()
