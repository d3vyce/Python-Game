from ast import Break, Global
import pygame
from pygame.locals import *
import src.level as level
import src.snake as snake
import src.window as window

LEVEL = 1
HEIGH = 10
WIDTH = 20
MATRIX = level.init_level(HEIGH, WIDTH)

def main():
    global MATRIX
    L_snake = snake.List((5, 5), None)
    L_snake = snake.List.List_add(L_snake, (5, 4))
    L_snake = snake.List.List_add(L_snake, (5, 3))
    L_snake = snake.List.List_add(L_snake, (5, 2))
    print(L_snake)
    print("Size : ", snake.List.List_size(L_snake))
    
    MATRIX[5][5] = 1
    MATRIX[5][4] = 1
    MATRIX[5][3] = 1
    MATRIX[5][2] = 1

    MATRIX[5][6] = 3
    level.spawn_apple(MATRIX, HEIGH, WIDTH)
    print(MATRIX)

    try:
        L_snake, MATRIX = snake.Snake_move(MATRIX, L_snake, "up")
    except ValueError as Error:
        if Error.args[0] == 1:
            print("You take a wall !")
        elif Error.args[0] == 2:
            print("You ate your tale !")
        
        exit()
    
    
    print(L_snake)
    print(MATRIX)


if __name__ == "__main__":
    main()