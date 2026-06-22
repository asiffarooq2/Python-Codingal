import pygame
import random

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Game with Background and Sound")

background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)

shoot_sound = pygame.mixer.Sound("laser.wav")
hit_sound = pygame.mixer.Sound("explosion.wav")

font = pygame.font.Font(None, 50)


class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


all_sprites = pygame.sprite.Group()

player = Sprite((0, 0, 0), 30, 30)
player.rect.x = random.randint(0, SCREEN_WIDTH - 30)
player.rect.y = random.randint(0, SCREEN_HEIGHT - 30)

target = Sprite((255, 0, 0), 30, 30)
target.rect.x = random.randint(0, SCREEN_WIDTH - 30)
target.rect.y = random.randint(0, SCREEN_HEIGHT - 30)

all_sprites.add(player)
all_sprites.add(target)

score = 0
won = False
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False

    if not won:
        keys = pygame.key.get_pressed()

        dx = 0
        dy = 0

        if keys[pygame.K_LEFT]:
            dx = -5
            shoot_sound.play()

        if keys[pygame.K_RIGHT]:
            dx = 5
            shoot_sound.play()

        if keys[pygame.K_UP]:
            dy = -5
            shoot_sound.play()

        if keys[pygame.K_DOWN]:
            dy = 5
            shoot_sound.play()

        player.move(dx, dy)

        if player.rect.colliderect(target.rect):
            hit_sound.play()
            score += 1

            target.rect.x = random.randint(0, SCREEN_WIDTH - 30)
            target.rect.y = random.randint(0, SCREEN_HEIGHT - 30)

            if score >= 5:
                won = True

    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    if won:
        win_text = font.render("YOU WIN!", True, (255, 255, 0))
        win_rect = win_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(win_text, win_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
