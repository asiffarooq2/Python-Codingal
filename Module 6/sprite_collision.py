import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5
FONT_SIZE = 50

pygame.init()

background_image = pygame.image.load("bg.jpg")
background_image = pygame.transform.scale(
    background_image, (SCREEN_WIDTH, SCREEN_HEIGHT)
)

font = pygame.font.SysFont("Times New Roman", FONT_SIZE)


class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill("dodgerblue")
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change

        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(
            0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")

all_sprites = pygame.sprite.Group()

sprite1 = Sprite("black", 20, 30)
sprite1.rect.x = random.randint(0, SCREEN_WIDTH - sprite1.rect.width)
sprite1.rect.y = random.randint(0, SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1)

sprite2 = Sprite("red", 20, 30)
sprite2.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite2.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)

running = True
won = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False

    if not won:
        keys = pygame.key.get_pressed()

        x_change = 0
        y_change = 0

        if keys[pygame.K_LEFT]:
            x_change = -MOVEMENT_SPEED
        if keys[pygame.K_RIGHT]:
            x_change = MOVEMENT_SPEED
        if keys[pygame.K_UP]:
            y_change = -MOVEMENT_SPEED
        if keys[pygame.K_DOWN]:
            y_change = MOVEMENT_SPEED

        sprite1.move(x_change, y_change)

        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True

    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    if won:
        text = font.render("You win!", True, (255, 255, 255))
        text_rect = text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(90)

pygame.quit()
