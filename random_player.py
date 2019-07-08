import numpy as np

class RandomPlayer:
    @staticmethod
    def give_move(moves, board):
        return moves[np.random.choice(len(moves))]