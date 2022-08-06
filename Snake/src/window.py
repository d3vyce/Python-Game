import pygame
from pygame.locals import *

def init_game():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((1000, 525), pygame.SCALED)
    pygame.display.set_caption("Snake")

    return screen

def draw_level(S, M, difficulty, score, fps, heigh, width):
    WHITE = (255, 255, 255) # AIR
    GREEN = (0, 255, 0)     # SNAKE
    BROWN = (255,248,220)   # WALL
    RED = (255, 0, 0)       # APPLE

    # Reset screen
    pygame.draw.rect(S, (0, 0, 0), pygame.Rect(0, 0, 1000, 525))
    
    my_font = pygame.font.SysFont('Comic Sans MS', 18)

    # Add FPS counter
    text_fps = my_font.render(str(fps) + ' fps', False, (255, 255, 255))
    S.blit(text_fps, (10, 0))
    
    # Add Score
    text_score = my_font.render('Score : '+ str(score), False, (255, 255, 255))
    S.blit(text_score, (400, 0))

    # Add Diffucilty
    text_difficulty = my_font.render('Difficulty : '+ str(difficulty), False, (255, 255, 255))
    S.blit(text_difficulty, (850, 0))

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