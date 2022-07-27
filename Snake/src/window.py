import pygame
from pygame.locals import *

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720), pygame.SCALED)
    pygame.display.set_caption("Test Window")

    return screen