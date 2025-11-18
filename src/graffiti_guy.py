import pygame
import math
import random

# player class

# enemy class - 

# platform class?

# canvas class - set up interactables for spraying on walls

# core game loop
def main():
    pygame.init()
    pygame.display.set_caption("Graffiti Guy")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        pygame.display.flip()
        dt = clock.tick(12)
    pygame.quit()

if __name__ == "__main__":
    main()