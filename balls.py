import random

import pygame

import movable_player


#  класс вражеского шарика
class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, type='blue', speed=5):
        super().__init__(all_sprites)

        self.type = type
        self.x, self.y = x, y
        self.speed = speed
        self.r = 0
        self.f = 0
        self.f_after_hit = 100
        self.radius = radius
        self.collided = 0

        #  спрайт шарика
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color(type), (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.mask = pygame.mask.from_surface(self.image)

        self.vx = random.randint(-speed, speed)
        self.vy = random.randint(-speed, speed)

    #  обновление шарика
    def update(self, player, f):

        if f < 2:
            self.kill()

        #  перемещение шарика
        self.rect = self.rect.move(self.vx, self.vy)

        #  столкновение шарика с игроком
        if pygame.sprite.spritecollide(self, movable_player.ball,
                                       False) and self.f_after_hit > 100 and self.f < 300:

            if player.mup and player.mright:
                self.vy -= player.speed // 1.25 * (self.speed // 3)
                self.vx = player.speed // 1.25 * (self.speed // 3)
            elif player.mup and player.mleft:
                self.vy -= player.speed // 1.25 * (self.speed // 3)
                self.vx -= player.speed // 1.25 * (self.speed // 3)
            elif player.mdown and player.mright:
                self.vy = player.speed // 1.25 * (self.speed // 3)
                self.vx = player.speed // 1.25 * (self.speed // 3)
            elif player.mdown and player.mleft:
                self.vy = player.speed // 1.25 * (self.speed // 3)
                self.vx -= player.speed // 1.25 * (self.speed // 3)
            elif player.mup:
                self.vy -= player.speed * 3
            elif player.mdown:
                self.vy = player.speed * 3
            elif player.mright:
                self.vx = player.speed * 3
            elif player.mleft:
                self.vx -= player.speed * 3
            else:
                self.vy = -self.vy
                self.vx = -self.vx
            self.collided = 1
            self.f_after_hit = 0

            #  последствия столкновения с игроком
            if player.f_after_hit > player.safe_frames:
                if self.f <= 300 and player.hp > 0 and player.started:
                    if self.type == 'blue':
                        player.f_after_hit = 0
                        player.hp -= 1
                        player.pts -= 20
                    elif self.type == 'black':
                        player.f_after_hit = 0
                        player.hp -= 1
                        player.pts += 30
                        player.speed = 6
                        player.size = 30
            if self.type == 'green':
                if 3 > player.hp > 0:
                    player.hp += 1
                player.pts += 20
            if self.type == 'pink':
                player.speed = 8
                player.size = 28
                player.pts += random.randint(0, 5)
            if self.type == 'brown':
                player.speed = 4
                player.size = 32
                player.pts -= random.randint(-5, 0)
            if self.type == 'crimson':
                player.speed = 5
                player.size = 35
                player.pts -= 25
            if self.type == 'gold':
                player.speed = 7
                player.size = 25
                player.pts += 25

        else:
            self.f_after_hit += 1

        #  исчезновение шарика
        if self.f == 500:
            self.kill()
        elif self.f > 300 and self.f % 3 == 0 or self.collided and self.f % 3 == 0 or player.hp == 0 \
                or not player.started:
            try:
                self.r -= 1
                radius = self.radius + self.r
                self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
                pygame.draw.circle(self.image, pygame.Color(self.type), (radius, radius), radius)
                self.rect = pygame.Rect(self.rect.x, self.rect.y, 2 * radius, 2 * radius)
            except:
                pass

        if self.rect.x < -1000 or self.rect.x > 2000 or self.rect.y < -1000 or self.rect.y > 2000:
            self.kill()

        self.f += 1


all_sprites = pygame.sprite.Group()
