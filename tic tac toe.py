#Imports
import pygame, sys
import numpy as np

#Constants and variables and inits
pygame.init()
board = np.zeros((3,3))
player = 1

SCREEN_SIZE = (600,600)
BACKGROUND = (30, 33, 38)
LINE_COLOR = (189, 94, 21)
SPACE = 50
CIRCLECOLOR = (184, 196, 209)
XCOLOR = (100, 114, 130)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BACKGROUND)


#Function defs

def draw_grid():
    pygame.draw.line(screen, LINE_COLOR, (200, 5), (200, 595), 4 )
    pygame.draw.line(screen, LINE_COLOR, (400, 5), (400, 595), 4 )
    pygame.draw.line(screen, LINE_COLOR, (5, 200), (595, 200), 4 )
    pygame.draw.line(screen, LINE_COLOR, (5, 400), (595, 400), 4 )

#drawign the Xs and Os
def draw_shape():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLECOLOR, (int(col*200+100), int(row*200+100)) , 60, 10)
            elif board[row][col] == 2:
                pygame.draw.line(screen, XCOLOR , (col*200+SPACE, row*200+200-SPACE) , (col*200+200-SPACE, row*200+SPACE), 20)
                pygame.draw.line(screen, XCOLOR , (col*200+SPACE, row*200+SPACE) , (col*200+200-SPACE, row*200+200-SPACE) , 20)

#make a play
def mark_sqr(row, col, player):
    board[row][col] = player
    print(board)

def available_sqr(row, col):
    return board[row][col] == 0

def fullBoard():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True

def win(player):
    pass

def draw_win():
    pass    

def restart():
    pass

#main loop
draw_grid()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clickedRow = int(mouseY//200)
            clickedCol = int(mouseX//200)
            if available_sqr(clickedRow, clickedCol):
                mark_sqr(clickedRow, clickedCol, player)
                draw_shape()
                if player == 1:
                    player = 2
                else:
                    player = 1

    pygame.display.update()