import pygame
from pygame.locals import *

RESOLUTION = (1280, 720)
DIFFICULTY = 1

Color_white = (255, 255, 255)
Color_Black = (0, 0, 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720), pygame.SCALED)
    pygame.display.set_caption("Test Window")

    width = screen.get_width()
    height = screen.get_height()

    font = pygame.font.SysFont('Corbel', 35)

    test = font.render('quit' , True , Color_Black)

    clock = pygame.time.Clock()
    live = True

    while live:
        # Set clock tick to 60 fps
        clock.tick(60)
        
        # 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                live = False
        
        screen.fill(Color_white)
        screen.blit(test , (width/2,height/2))

        # Draw Scene
        pygame.display.flip()

        # Display current fps
        print(float("{0:.2f}".format(clock.get_fps())), 'fps')


if __name__ == "__main__":
    main()