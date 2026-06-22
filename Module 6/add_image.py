import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Penguin Game")

background = pygame.image.load("background.png").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

penguin = pygame.image.load("penguin.png").convert_alpha()
penguin = pygame.transform.scale(penguin, (200, 200))

penguin_rect = penguin.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

font = pygame.font.Font(None, 36)
text = font.render("Hello World", True, (0, 0, 0))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 50))


def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 0))
        screen.blit(penguin, penguin_rect)
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    game_loop()
