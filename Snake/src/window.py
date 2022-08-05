import pygame
from pygame.locals import *

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 525), pygame.SCALED)
    pygame.display.set_caption("Snake")

    return screen

def draw_level(S, M, difficulty, score, heigh, width):
    WHITE = (255, 255, 255) # AIR
    GREEN = (0, 255, 0)     # SNAKE
    BROWN = (255,248,220)   # WALL
    RED = (255, 0, 0)       # APPLE

    Color = WHITE

    for j in range(heigh):
        for i in range(width):
            if M[j][i] == 0:
                Color = WHITE
            elif M[j][i] == 1:
                Color = GREEN
            elif M[j][i] == 2:
                Color = BROWN
            elif M[j][i] == 3:
                Color = RED

            pygame.draw.rect(S, Color, pygame.Rect(i*25, j*25+25, 25, 25))
    
    return S