import numpy as np
import random

# 0 = AIR
# 1 = SNAKE
# 2 = WALL
# 3 = APPLE

def init_level(heigh, width):
    return np.zeros((heigh, width))

def spawn_apple(M, heigh, width):
    random.seed()
    rand_heigh = random.randrange(0, heigh)
    rand_width = random.randrange(0, width)

    if M[rand_heigh][rand_width] == 0:
        M[rand_heigh][rand_width] = 3
    else:
        spawn_apple(M, heigh, width)
    