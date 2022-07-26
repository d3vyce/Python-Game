import pygame
from pygame.locals import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720), pygame.SCALED)
    pygame.display.set_caption("Test Window")

    clock = pygame.time.Clock()
    live = True
    x = 0

    while live:
        # Set clock tick to 60 fps
        clock.tick(60)
        
        # 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                live = False

        # Change background color
        if x == 255: x = 0
        else: x += 1
        screen.fill((x, 0, 0))
        
        # Draw Scene
        pygame.display.flip()

        # Display current fps
        print(float("{0:.2f}".format(clock.get_fps())), 'fps')


if __name__ == "__main__":
    main()