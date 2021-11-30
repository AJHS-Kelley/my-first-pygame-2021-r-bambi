# my first PyGame, Bambi Romedy, 11/30/21, 12:14pm, v0.3

import pygame, sys
from pygame.locals import *

# Initialize PyGame
pygame.init()

# set up the window to draw on.
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('My First PyGame')

# setup color values. (r, g, b)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LUNA = (195, 159, 255)