from ast import Break
import pygame
from pygame.locals import *
import src.level as level
import src.snake as snake
import src.window as window

LEVEL = 1
HEIGH = 10
WIDTH = 20

def main():
    L_snake = snake.List((5, 5), None)
    L_snake = snake.List.List_add(L_snake, (5, 4))
    L_snake = snake.List.List_add(L_snake, (5, 3))
    L_snake = snake.List.List_add(L_snake, (5, 2))
    print(L_snake)
    print("Size : ", snake.List.List_size(L_snake))
    

    matrix = level.init_level(HEIGH, WIDTH)
    matrix[5][5] = 1
    matrix[5][6] = 1
    level.spawn_apple(matrix, HEIGH, WIDTH)
    #print(matrix)

    try:
        L_snake = snake.Snake_move(matrix, L_snake, "right")
    except ValueError as Error:
        if Error.args[0] == 1:
            print("You take a wall !")
        elif Error.args[0] == 2:
            print("You ate your tale !")
        
        exit()
    
    
    print(L_snake)


if __name__ == "__main__":
    main()