import pygame
import sys
import numpy as np
from constants import *

# section of pygame
pygame.init()
screen = pygame.display.set_mode((width, HIGHT))
pygame.display.set_caption('Tic Tac Toe Game')
screen.fill(BG_COLOR)


class Board:
    def __init__(self):
        self.squares = np.zeros((ROW, COLS))

    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player

    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0


class Game:

    def __init__(self):
        self.board = Board()
        self.player = 1
        self.show_lines()

    def show_lines(self):  # for drawing vertical and horizontal line
        # vertical
        pygame.draw.line(screen, Line_Color, (Squaresize, 0),
                         (Squaresize, HIGHT), Line_width)
        pygame.draw.line(screen, Line_Color, (width-Squaresize, 0),
                         (width-Squaresize, HIGHT), Line_width)
        # horizontal
        pygame.draw.line(screen, Line_Color, (0, Squaresize),
                         (width, Squaresize), Line_width)
        pygame.draw.line(screen, Line_Color, (0, HIGHT-Squaresize),
                         (width, HIGHT-Squaresize), Line_width)


def main():
    game = Game()
    board = game.board

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // Squaresize
                col = pos[0] // Squaresize
           

        pygame.display.update()


main()
