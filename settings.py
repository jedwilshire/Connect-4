import pygame
BOXSIZE = 60

BOARDWIDTH = 7
BOARDHEIGHT = 6

WIDTH = BOXSIZE * BOARDWIDTH
HEIGHT = BOXSIZE * BOARDHEIGHT
TITLE = 'Connect 4!'
FPS = 60

#            R    G    B
BLACK    = (  0,   0,   0)
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE

def makeList(row, col):
    board = []
    for i in range(row):
        board.append([])
        for k in range(col):
            board[i].append(None)
    return board
# Not needed idea
# ARROW = pygame.Surface((BOXSIZE, BOXSIZE))
# pygame.draw.polygon(ARROW, BLACK,
#                  [[20, 10], [40, 10], [40, 40], [50, 40], [30, 50], [20, 40], [20, 10]])