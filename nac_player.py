import numpy as np
from copy import deepcopy

class Node:
    def __init__(self, move = None, our_turn = True, value = -1000, children = []):
        self.move = move
        self.our_turn = our_turn
        self.value = value
        self.children = children

class NACAlphaBetaPlayer:
    def __init__(self, player = 1):
        self.player = player
        self.opponent = 3 - player
        
    @staticmethod
    def check_array_elements_same(arr):
        return np.all(arr == arr[0])

    def check_win(self, board, player):
        if self.check_array_elements_same(board[0]) and board[0,0] != 0:
            return 1 if board[0,0] == player else -1
        if self.check_array_elements_same(board[1]) and board[1,0] != 0:
            return 1 if board[1,0] == player else -1
        if self.check_array_elements_same(board[2]) and board[2,0] != 0:
            return 1 if board[2,0] == player else -1
        if self.check_array_elements_same(board[0:3,0]) and board[0,0] != 0:
            return 1 if board[0,0] == player else -1
        if self.check_array_elements_same(board[0:3,1]) and board[0,1] != 0:
            return 1 if board[0,1] == player else -1
        if self.check_array_elements_same(board[0:3,2]) and board[0,2] != 0:
            return 1 if board[0,2] == player else -1
        if self.check_array_elements_same([board[0,0], board[1,1], board[2,2]]) and board[0,0] != 0:
            return 1 if board[0,0] == player else -1
        if self.check_array_elements_same([board[2,0], board[1,1], board[0,2]]) and board[2,0] != 0:
            return 1 if board[2,0] == player else -1
        if 0 not in np.ndarray.flatten(board):
            return 0
        return -2
    
    @staticmethod
    def get_moves_from_board(board):
        moves = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row,col] == 0:
                    moves.append((row,col))
        return moves
    
    def simulate_board(self, board, move, opponents_move = False):
        adjusted_board = deepcopy(board)
        adjusted_board[move] = self.player if not opponents_move else self.opponent
        return adjusted_board
    
    def alpha_beta(self, board, alpha, beta, maximising_player):
        value = self.check_win(board, self.player)# if maximising_player else self.check_win(board, self.opponent)
        if value != -2:
            return value
        moves = self.get_moves_from_board(board)
        if maximising_player:
            value = -float('inf')
            for move in moves:
                adjusted_board = self.simulate_board(board, move, False)
                value = max(value, self.alpha_beta(adjusted_board, alpha, beta, False))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value
        else:
            value = float('inf')
            for move in moves:
                adjusted_board = self.simulate_board(board, move, True)
                value = min(value, self.alpha_beta(adjusted_board, alpha, beta, True))
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return value
            
    def give_move(self, moves, board):
        if self.check_array_elements_same(np.ndarray.flatten(board)):
            return (1,1) if np.random.uniform() < 0.3 else [(0,0),(2,0),(0,2),(2,2)][np.random.choice(4)]
        current_move = moves[0]
        current_value = self.alpha_beta(self.simulate_board(board, current_move, False), -float('inf'), float('inf'), False)
        for move in moves[1:]:
            candidate_value = self.alpha_beta(self.simulate_board(board, move, False), -float('inf'), float('inf'), False)
            if candidate_value + np.random.uniform(-0.1,0.1) > current_value:
                current_move, current_value = move, candidate_value
        return current_move
    
    
class NACQlearnPlayer():
    filename = "NAC_qtable.csv"
    
    def __init__(self, player = 1):
        self.player = player
        self.opponent = 3 - player
        self.Q = np.genfromtxt(self.filename, delimiter=",")
        self.moves = []
        
        self.learning_rate = 0.9
        self.discount_factor = 0.95
        
    @staticmethod
    def hash_board(board):
        hash_val = 0
        for x in np.ndarray.flatten(board):
            hash_val *= 3
            hash_val += x
        return int(hash_val)
    
    @staticmethod
    def unhash_board(hash_val):
        temp_hash = deepcopy(hash_val)
        board = np.zeros((3,3))
        for i in [8,7,6,5,4,3,2,1,0]:
            board[i // 3, i % 3] = temp_hash % 3
            temp_hash -= temp_hash % 3
            temp_hash /= 3
        return board
    
    @classmethod
    def add_move_to_hash(cls, hash_val, move):
        board = cls.unhash_board(hash_val)
        board[move // 3, move % 3] = (np.count_nonzero(board) % 2) + 1
        return cls.hash_board(board)
    
    def reset_game(self):
        self.moves = []
    
    def update_Q(self, value_of_last_state):
        discount = 1
        self.Q[self.moves[-1]] = value_of_last_state
        for sa in self.moves[:-1:-1]:
            self.Q[sa] = (1 - self.learning_rate)*self.Q[sa] + self.learning_rate * discount * np.max([self.Q[self.add_move_to_hash(sa[0], a)] for a in [0,1,2,3,4,5,6,7,8]])
            discount *= self.discount_factor
        #np.savetxt(self.filename, self.Q, delimiter=",")
        
    def save_Q(self):
        np.savetxt(self.filename, self.Q, delimiter=",")        

    def give_move(self, moves, board):
        s = self.hash_board(board)
        while True:
            a = np.argmax(self.Q[s])
            move = (a // 3, a % 3)
            if move in moves:
                self.moves.append((s,a))
                return move
            self.Q[s,a] = -2
            
class NACQlearnPlayer1(NACQlearnPlayer):
    filename = "NAC_qtable1.csv"
    
class NACQlearnPlayer2(NACQlearnPlayer):
    filename = "NAC_qtable2.csv"