#Imports
import copy
import pygame, sys
import numpy as np
from pickletools import pyfloat
import random
import re
from telnetlib import GA

#Constants and variables and inits
pygame.init()
board = np.zeros((3,3))
player = 1
turn = True
GameOver = False

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
def drawMenu():
    color = (184, 196, 209)
    color_light = (170,170,170)
    color_dark = (100,100,100)

    width = 600
    height = 600
    smallfont = pygame.font.SysFont('Corbel',35)

    text = smallfont.render('Two Players' , True , color)
    text2 = smallfont.render('Easy AI' , True , color)
    text4 = smallfont.render('Impossible AI' , True , color)
    text3 = smallfont.render('QUIT' , True , color)
    
    while True:
        
        for ev in pygame.event.get():
            
            if ev.type == pygame.QUIT:
                pygame.quit()
                
            #checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                
                #if the mouse is clicked on the
                # button the game is terminated
                if 170 <= mouse[0] <= 170+250 and 95 <= mouse[1] <= 95+50:
                    twoPlayerLoop()
                elif 170 <= mouse[0] <= 170+250 and 155 <= mouse[1] <= 155+50:
                    vsRandAILoop()
                elif 170 <= mouse[0] <= 170+250 and 215 <= mouse[1] <= 215+50:
                    vsAILoop()
                elif 170 <= mouse[0] <= 170+250 and 350 <= mouse[1] <= 350+50:
                    sys.exit()
                    
        # fills the screen with a color
        screen.fill(BACKGROUND)
        
        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()
        
        pygame.draw.rect(screen,color_dark,[170,95,250,50])
        pygame.draw.rect(screen,color_dark,[170,155,250,50])
        pygame.draw.rect(screen,color_dark,[170,215,250,50])
        pygame.draw.rect(screen,color_dark,[170,350,250,50])
        
        # superimposing the text onto our button
        screen.blit(text , (210,100))
        screen.blit(text2 , (245,160))
        screen.blit(text4 , (205,220))
        screen.blit(text3 , (250,360))
        
        # updates the frames of the game
        pygame.display.update()

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
def mark_sqr(board, row, col, player):
    board[row][col] = player

def available_sqr(row, col):
    return board[row][col] == 0

def getEmptySqr(board):
    emptySqr = []
    for row in range(3):
        for col in range(3):
            if available_sqr(row, col):
                emptySqr.append((row, col))
    return emptySqr

def fullBoard():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True

def win(player):
    #vertical win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            draw_win_vert(col, player)
            return True
    #horizontal win
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            draw_win_hor(row, player)
            return True
    #diagnoal win
    if board[0][0] == board[1][1] == board[2][2] == player:
        draw_win_diag(1, player)
        return True
    if board[2][0] == board[1][1] == board[0][2] == player:
        draw_win_diag(2, player)
        return True
    return False

def draw_win_vert(col, player):
    posx = col*200+100
    if player == 1:
        color = XCOLOR
    elif player == 2:
        color = CIRCLECOLOR
    pygame.draw.line(screen, color, (posx, 15), (posx, 600-15), 10)

def draw_win_hor(row, player):
    posy = row*200+100
    if player == 1:
        color = XCOLOR
    elif player == 2:
        color = CIRCLECOLOR
    pygame.draw.line(screen, color, (15 , posy), (600-15, posy), 10)    

def draw_win_diag(dir, player):
    if player == 1:
        color = XCOLOR
    elif player == 2:
        color = CIRCLECOLOR
    if dir == 2:
        pygame.draw.line(screen, color, (20, 600-20), (600-20, 20), 10)
    elif dir == 1:
        pygame.draw.line(screen, color, (20, 20), (600-20, 600-20), 10)

def restart():
    screen.fill(BACKGROUND)
    draw_grid()
    player = 2
    for row in range(3):
        for col in range(3):
            board[row][col] = 0

def twoPlayerLoop():
    global player
    global GameOver
    screen.fill(BACKGROUND)
    draw_grid()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not GameOver:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clickedRow = int(mouseY//200)
                clickedCol = int(mouseX//200)
                if available_sqr(clickedRow, clickedCol):
                    mark_sqr(board, clickedRow, clickedCol, player)
                    draw_shape()
                    if win(player):
                        GameOver = True
                        print(GameOver)
                    if player == 1:
                        player = 2
                    else:
                        player = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    restart()
                    GameOver = False
                elif event.key == pygame.K_ESCAPE:
                    drawMenu()

        pygame.display.update()

def RandEval():
    global turn
    global GameOver
    board
    emptysqr = getEmptySqr(board)
    if len(emptysqr) == 0:
        GameOver = True
    elif not GameOver:
       idx = random.randrange(0, len(emptysqr))
       sqr = emptysqr[idx]
       mark_sqr(board, sqr[0], sqr[1], 2)
       draw_shape()
       if win(2):
            GameOver = True
       turn = True

def mmMove(move):
    global turn
    global GameOver
    global board
    emptysqr = getEmptySqr(board)
    if len(emptysqr) == 0:
        GameOver = True
    elif not GameOver:  
       mark_sqr(board, move[0], move[1], 2)
       draw_shape()
       if win(2):
            GameOver = True
       turn = True

def minimax(board, max):
    case = finalState()
    if case == 1:
        return 1, None
    elif case == 2:
        return -1, None
    elif fullBoard():
        return 0, None
    if max:
        maxEval = -100
        bestMove = None
        emptySqrs = getEmptySqr(board)
        for (row, col) in emptySqrs:
            tBoard = copy.deepcopy(board)
            mark_sqr(tBoard, row, col, 1)
            eval = minimax(tBoard, False)[0]
            print(eval)
            if eval > maxEval:
                maxEval = eval
                bestMove = (row, col)
        return maxEval, bestMove
    elif not max:
        minEval = 100
        bestMove = None
        emptySqrs = getEmptySqr(board)
        for (row, col) in emptySqrs:
            tBoard = copy.deepcopy(board)
            mark_sqr(tBoard, row, col, 2)
            eval = minimax(tBoard, True)[0]
            print(eval)
            if eval < minEval:
                minEval = eval
                bestMove = (row, col)
        return minEval, bestMove

def finalState():
    if win(1):
        return 1
    elif win(2):
        return 2
    else:
        return 0

def vsRandAILoop():
    global turn
    global board
    global player
    global GameOver
    screen.fill(BACKGROUND)
    draw_grid()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and turn and not GameOver:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clickedRow = int(mouseY//200)
                clickedCol = int(mouseX//200)
                if available_sqr(clickedRow, clickedCol):
                    mark_sqr(board, clickedRow, clickedCol, 1)
                    draw_shape()
                    if win(1):
                        GameOver = True
                turn = False
                RandEval()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    restart()
                    GameOver = False
                    turn = True
                elif event.key == pygame.K_ESCAPE:
                    drawMenu()

        pygame.display.update()

def vsAILoop():
    global turn
    global board
    global player
    global GameOver
    player = 1
    screen.fill(BACKGROUND)
    draw_grid()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and turn and not GameOver:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clickedRow = int(mouseY//200)
                clickedCol = int(mouseX//200)
                if available_sqr(clickedRow, clickedCol):
                    mark_sqr(board, clickedRow, clickedCol, 1)
                    draw_shape()
                    if win(1):
                        GameOver = True
                turn = False
                eval, move = minimax(board, False)
                print(eval)
                mmMove(move)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    restart()
                    GameOver = False
                    turn = True
                elif event.key == pygame.K_ESCAPE:
                    drawMenu()

        pygame.display.update()

#main loop
drawMenu()