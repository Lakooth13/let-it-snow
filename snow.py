# Simple pygame program

# Import and initialize the pygame library
import pygame
import random

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Let it snow ❄️")

WIDTH = 600
HEIGHT = 400
FALL_SPEED = 3
MAX_SNOW_SIZE = 5
NUM_SNOW = WIDTH//4
snow_list = []

for i in range(NUM_SNOW):
    snow_list.append([
        random.randrange(0, WIDTH),
        random.randrange(0, HEIGHT),
        random.randrange(0, MAX_SNOW_SIZE),
        random.randrange(-1, 2)
    ])

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((0, 0, 0))

    for particle in snow_list:

        # make snow fall
        particle[1] += FALL_SPEED

        # make snow drift left or right
        particle[0] += particle[3]

        # detect if snow has fallen past end of screen, and recycle
        if particle[1] > HEIGHT:
            particle[1] = 0

        # detect if snow has fallen past sides of screen, and recycle
        if particle[0] > WIDTH:
            particle[0] = 0
        if particle[0] < 0:
            particle[0] = WIDTH


    # draw snow particles
    for particle in snow_list:
        pygame.draw.circle(screen, (255, 255, 255), (particle[0], particle[1]), particle[2])

    # Flip the display
    pygame.display.flip()

    clock.tick(40)

# Done! Time to quit.
pygame.quit()
