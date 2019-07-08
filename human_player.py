import pygame
import sys

class Human:
    def __init__(self, player):
        pass
    
    @staticmethod
    def give_move(moves, board):
        while True:
            row = int(input("Enter row number: "))
            col = int(input("Enter column number: "))
            if (row, col) in moves:
                return (row, col)
            
class HumanVisual(Human):
    @staticmethod
    def give_move(moves, board):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    pos = (int(pos[1]/100), int(pos[0]/100))
                    if pos in moves:
                        return pos