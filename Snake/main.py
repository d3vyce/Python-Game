from ast import Break, Global
import pygame
from pygame.locals import *
import src.level as level
import src.snake as snake
import src.window as window

HEIGH = 20
WIDTH = 40

def main():
    # Init Matrix/Window
    Matrix = level.init_level(HEIGH, WIDTH)
    Screen = window.init_game()

    # Init Game Variables
    clock = pygame.time.Clock()
    Running = True
    Direction = 'right'
    Direction_prev = 'right'
    Move_loop = 10
    Score = 0
    Difficulty = 1
    Fruit = False

    # Spawn snake head
    L_snake = snake.List((5, 5), None)

    # Spawn first apple
    level.spawn_apple(Matrix, HEIGH, WIDTH)

    while Running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                Running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                Direction = 'right'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                Direction = 'left'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                Direction = 'up'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                Direction = 'down'

        if Move_loop == 0:
            if Direction == 'left' and Direction_prev == 'right' or Direction == 'right' and Direction_prev == 'left' or Direction == 'up' and Direction_prev == 'down' or Direction == 'down' and Direction_prev == 'up':
                Direction = Direction_prev

            try:
                L_snake, Matrix, Fruit, Score = snake.Snake_move(Matrix, L_snake, Direction, Score, HEIGH, WIDTH)
            except ValueError as Error:
                if Error.args[0] == 1:
                    print("You take a wall !")
                elif Error.args[0] == 2:
                    print("You ate your tale !")
                exit()
            
            if Fruit:
                level.spawn_apple(Matrix, HEIGH, WIDTH)
            
            Direction_prev = Direction
            if(Score > 1000):
                Difficulty = int(Score/1000) + 1
            Move_loop = 11 - Difficulty

        Move_loop -= 1

        # Draw Scene
        Screen = window.draw_level(Screen, Matrix, Difficulty, Score, int(clock.get_fps()), HEIGH, WIDTH)
        pygame.display.flip()

        # Print current fps
        print(float("{0:.2f}".format(clock.get_fps())), 'fps')


if __name__ == "__main__":
    main()