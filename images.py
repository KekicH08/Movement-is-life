import pygame

pygame.init()


#  загрузка графических файлов
def load_image(name, color_key=None):
    fullname = name
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


#  класс картинки сердца
class Heart(pygame.sprite.Sprite):
    image = load_image("heart.png", -1)

    def __init__(self, number, player):
        super().__init__(all_sprites)
        self.player = player
        self.image = Heart.image
        self.image = pygame.transform.scale(self.image, (65, 65))
        self.rect = pygame.Rect(65 * number, 10, 65, 65)
        self.rect.x -= 50
        self.mask = pygame.mask.from_surface(self.image)


#  класс картинки грустного смайлика
class Sad_smile(pygame.sprite.Sprite):
    image = load_image("sad_smile.png", -1)

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Sad_smile.image
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = pygame.Rect(10, 10, 65, 65)
        self.mask = pygame.mask.from_surface(self.image)


all_sprites = pygame.sprite.Group()
