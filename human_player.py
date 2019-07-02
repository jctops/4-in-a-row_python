import pygame
import sys

class Human:
    @staticmethod
    def give_move(moves):
        while True:
            row = int(input("Enter row number: "))
            col = int(input("Enter column number: "))
            if (row, col) in moves:
                return (row, col)
            
class HumanVisual:
    @staticmethod
    def give_move(moves):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    return (int(pos[1]/100), int(pos[0]/100))