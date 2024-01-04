import pygame


#  класс игрового персонажа
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, color='red', size=30, hp=3, speed=6, name='undefined', safe_frames=70):
        super().__init__(all_sprites)

        self.add(ball)
        self.name = name
        self.pos = pos
        self.color = color
        self.size = size
        self.hp = hp
        self.speed = speed
        self.started = False
        self.mup, self.mdown, self.mright, self.mleft = False, False, False, False

        #  спрайт игрока
        self.image = pygame.Surface((2 * size, 2 * size), pygame.SRCALPHA, 32)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = pygame.Rect(self.pos[0] - size // 1.5, self.pos[1] - size // 1.5, size // 0.75, size // 0.75)

        self.safe_frames = safe_frames
        self.f_after_hit = safe_frames

        self.pts = 0

    def update(self):
        #  движение игрока
        if self.mup and self.mright:
            self.pos[1] -= self.speed // 1.25
            self.pos[0] += self.speed // 1.25
        elif self.mup and self.mleft:
            self.pos[1] -= self.speed // 1.25
            self.pos[0] -= self.speed // 1.25
        elif self.mdown and self.mright:
            self.pos[1] += self.speed // 1.25
            self.pos[0] += self.speed // 1.25
        elif self.mdown and self.mleft:
            self.pos[1] += self.speed // 1.25
            self.pos[0] -= self.speed // 1.25
        elif self.mup:
            self.pos[1] -= self.speed
        elif self.mdown:
            self.pos[1] += self.speed
        elif self.mright:
            self.pos[0] += self.speed
        elif self.mleft:
            self.pos[0] -= self.speed
        self.pos = [abs(self.pos[0]), abs(self.pos[1])]
        self.rect.x, self.rect.y = self.pos[0] - self.size // 1.5, self.pos[1] - self.size // 1.5

        self.f_after_hit += 1


all_sprites = pygame.sprite.Group()
ball = pygame.sprite.Group()
