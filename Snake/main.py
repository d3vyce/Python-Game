import pygame
from pygame.locals import *
import src.level as level
import src.snake as snake
import src.window as window

LEVEL = 1
HEIGH = 10
WIDTH = 20

def main():
    test = snake.List((5, 5), None)
    test = snake.List.List_add(test, 12)
    test = snake.List.List_add(test, 14)
    test = snake.List.List_add(test, 16)
    print(test)
    print("Size : ", snake.List.List_size(test))

    matrix = level.init_level(HEIGH, WIDTH)
    matrix[5][5] = 1
    level.spawn_apple(matrix, HEIGH, WIDTH)
    print(matrix)



if __name__ == "__main__":
    main()