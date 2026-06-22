import pygame
import random

pygame.init()

COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COLOR_CHANGE_EVENT, 1000)

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Custom Event - Change Sprite Colors")


class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def change_color(self):
        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        self.image.fill(color)


sprite1 = Sprite((255, 0, 0), 60, 60, 150, 170)
sprite2 = Sprite((0, 0, 255), 60, 60, 350, 170)

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == COLOR_CHANGE_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
