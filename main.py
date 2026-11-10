import pygame
import sys

# INITIALIZES PYGAME
pygame.init()

# WINDOW DIMENSIONS
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TESTING")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("WHITE")

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()