import pygame
import random

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ant Colony Management Game")
clock = pygame.time.Clock()
running = True

# Ant colony variables
ants = []

class Ant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic

    # Spawn new ants randomly
    if random.random() < 0.01:
        ants.append(Ant(random.randint(0, 800), random.randint(0, 600)))

    # Draw the ants
    for ant in ants:
        ant.draw()

    # Flip the display to update the screen
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

pygame.quit()
