# Simple Animimation with Pygame, Bambi Romedy, 01/04/22, 1:17pm, v0.1

import pygame, sys, time 
from pygame.locals import

# Setup PyGame
pygame.init()

# Setup the Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowsurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')