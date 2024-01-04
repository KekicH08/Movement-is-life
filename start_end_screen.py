import pygame
import sys
import sqlite3
from operator import itemgetter


pygame.init()
screen_size = (1200, 800)
screen = pygame.display.set_mode(screen_size)
FPS = 60
running = True
clock = pygame.time.Clock()
pygame.display.set_caption('Movement is life')


#  выход
def terminate():
    pygame.quit()
    sys.exit()


#  экран при входе в игру
def start_screen():
    screen.fill((235, 255, 255))
    font = pygame.font.Font(None, 150)
    string_rendered = font.render('Movement is life', 1, pygame.Color('blue'))
    screen.blit(string_rendered, (180, 320, 1000, 500))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    end_screen()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return

        pygame.display.flip()
        clock.tick(FPS)


#  экран на выходе из игры
def end_screen():
    screen.fill((235, 255, 255))
    font = pygame.font.Font(None, 150)
    string_rendered = font.render('Goodbye!', 1, pygame.Color('purple'))
    screen.blit(string_rendered, (350, 320, 1000, 500))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return

        pygame.display.flip()
        clock.tick(FPS)


#  экран с таблицей лидеров
def leaderboard():
    LEADERBOARD = sqlite3.connect('leaderboard.db')
    TABLE = list(set(LEADERBOARD.cursor().execute('SELECT * FROM Leaders').fetchall()))
    TABLE.sort(key=lambda x: x[0])
    TABLE.sort(key=itemgetter(1, 2), reverse=True)

    while True:
        screen.fill((235, 255, 255))
        font = pygame.font.Font(None, 110)
        string_rendered = font.render('Leaders', 1, pygame.Color('crimson'))
        screen.blit(string_rendered, (20, 15, 1000, 200))

        font = pygame.font.Font(None, 60)
        string_rendered = font.render('Nickname', 1, pygame.Color('blue'))
        screen.blit(string_rendered, (20, 120, 300, 100))

        string_rendered = font.render('Level', 1, pygame.Color('blue'))
        screen.blit(string_rendered, (400, 120, 300, 100))

        string_rendered = font.render('Score', 1, pygame.Color('blue'))
        screen.blit(string_rendered, (550, 120, 300, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return

        font = pygame.font.Font(None, 50)
        i = 0
        for row in TABLE:
            i += 1
            string_rendered = font.render(str(i), 1, pygame.Color('red'))
            screen.blit(string_rendered, (10, 500 * i // 4.8 + 100, 40, 50))
            k = 0
            for line in row:
                k += 1
                string_rendered = font.render(str(line), 1, pygame.Color('purple'))
                if k == 3:
                    screen.blit(string_rendered, (550, 500 * i // 4.8 + 100, 200 * k, 50))
                else:
                    screen.blit(string_rendered, (50 + 350 * (k - 1), 500 * i // 4.8 + 100, 200 * k, 50))
            if i == 15:
                break
        pygame.display.flip()
        clock.tick(FPS)


start_screen()
