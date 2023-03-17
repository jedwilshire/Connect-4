from settings import *
from writer import *
import pygame
from pygame import Rect, Surface

# global variables
screen = pygame.display.set_mode((WIDTH, HEIGHT))
board = makeList(BOARDHEIGHT, BOARDWIDTH)  # makeList is a function defined in settings
turnCount = 0
winner = None
writer = Writer(screen, size = 40)
# set title from settings
pygame.display.set_caption(TITLE)

def make_board():
    for row in range(BOARDHEIGHT):
        for col in range(BOARDWIDTH):
            x = col
            y = row
            board[row][col] = make_spot(x, y)
    
def draw():
    screen.fill(BGCOLOR)
    for row in range(BOARDHEIGHT):
        for col in range(BOARDWIDTH):
            cell = board[row][col]
            screen.blit(cell.image, cell.rect)
    if winner != None:
        writer.write(winner + ' WINS!', WIDTH // 4, HEIGHT // 3)
    
    pygame.display.flip()

def get_dropped_row(col):
    row = 0
    while row < BOARDHEIGHT and board[row][col].checker == None:
        row += 1
    return row - 1

def on_mouse_down(pos):
    global turnCount
    col = pos[0] // BOXSIZE
    if winner == None and board[0][col].checker == None:
        row = get_dropped_row(col)
        cell = board[row][col]
        if turnCount % 2 == 0:
            pygame.draw.circle(cell.image, YELLOW, (BOXSIZE // 2, BOXSIZE // 2), BOXSIZE // 3)
            cell.checker = 'yellow'
        else:
            pygame.draw.circle(cell.image, RED, (BOXSIZE // 2, BOXSIZE // 2), BOXSIZE // 3)
            cell.checker = 'red'
        turnCount += 1
        
def update():
    global winner
    for row in range(BOARDHEIGHT):
        for col in range(BOARDWIDTH):
            win = checkUp(row, col) or checkLeft(row, col) or checkUpLeft(row, col) or checkUpRight(row, col)
            if win:
                winner = board[row][col].checker.upper()
                
                
def checkUp(row, col):
    if row < 3 or board[row][col].checker == None:
        return False
    else:
        c = board[row][col].checker
        return (c == board[row-1][col].checker and
                c == board[row-2][col].checker and
                c == board[row-3][col].checker) 

def checkLeft(row, col):
    if col < 3 or board[row][col].checker == None:
        return False
    else:
        c = board[row][col].checker
        return (c == board[row][col-1].checker and
                c == board[row][col-2].checker and
                c == board[row][col-3].checker)  
def checkUpLeft(row, col):
    if col < 3 or row < 3 or board[row][col].checker == None:
        return False
    else:
        c = board[row][col].checker
        return (c == board[row-1][col-1].checker and
                c == board[row-2][col-2].checker and
                c == board[row-3][col-3].checker) 

def checkUpRight(row, col):
    if col > 3 or row < 3 or board[row][col].checker == None:
        return False
    else:
        c = board[row][col].checker
        return (c == board[row-1][col+1].checker and
                c == board[row-2][col+2].checker and
                c == board[row-3][col+3].checker)
def mainloop():
    running = True
    clock = pygame.time.Clock()
    while running:
        update()
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                on_mouse_down(event.pos)
        clock.tick(FPS)

def make_spot(x, y):
    spot = pygame.sprite.Sprite()
    spot.image = Surface((BOXSIZE, BOXSIZE))
    spot.x = x
    spot.y = y
    spot.rect = pygame.Rect(x * BOXSIZE, y * BOXSIZE, BOXSIZE, BOXSIZE)
    spot.image.fill(BLUE)
    spot.checker = None
    pygame.draw.circle(spot.image, WHITE, (BOXSIZE // 2, BOXSIZE // 2), BOXSIZE // 3)
    return spot


make_board()
pygame.init()
mainloop()




