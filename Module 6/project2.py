import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")

font = pygame.font.Font(None, 36)
text = font.render("Hello World", True, (255, 255, 255))
text_rect = text.get_rect(center=(320, 100))

rect = pygame.Rect(270, 190, 100, 100)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 125, 255), rect)
    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()
