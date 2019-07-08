import numpy as np
from copy import deepcopy

class BasicParameterPlayer:
    C = 2
    w_c2iar = 1
    w_u2iar = 1
    w_3iar = 10
    w_4iar = 100
    w_center = 1    
    
    def __init__(self, player = 1):
        self.player = player
        self.opponent = 3 - player
        
    def evaluate_horizontal_c2iar(self, board):
        m = len(board)
        n = len(board[0])
        total = 0
        for row in range(m):
            for col in range(n-1):
                if board[row,col] == self.player:
                    if board[row,col+1] == self.player:
                        total += self.C * self.w_c2iar
                elif board[row,col] == self.opponent:
                    if board[row,col+1] == self.opponent:
                        total -= self.w_c2iar
        return total
        
    def evaluate_vertical_c2iar(self, board):
        m = len(board)
        n = len(board[0])
        total = 0
        for row in range(1,m):
            for col in range(n):
                if board[row,col] == self.player:
                    if board[row-1,col] == self.player:
                        total += self.C * self.w_c2iar
                elif board[row,col] == self.opponent:
                    if board[row-1,col] == self.opponent:
                        total -= self.w_c2iar
        return total
                        
    def evaluate_diagonal_c2iar(self, board):
        m = len(board)
        n = len(board[0])
        total = 0
        for row in range(1,m):
            for col in range(n-1):
                if board[row,col] == self.player:
                    if board[row-1,col+1] == self.player:
                        total += self.C * self.w_c2iar
                elif board[row,col] == self.opponent:
                    if board[row-1,col+1] == self.opponent:
                        total -= self.w_c2iar
        return total
    
    def evaluate_downdiagonal_c2iar(self, board):
        m = len(board)
        n = len(board[0])
        total = 0
        for row in range(m-1):
            for col in range(n-1):
                if board[row,col] == self.player:
                    if board[row+1,col+1] == self.player:
                        total += self.C * self.w_c2iar
                elif board[row,col] == self.opponent:
                    if board[row+1,col+1] == self.opponent:
                        total -= self.w_c2iar
        return total
                        
    def evaluate_c2iar(self, board):
        return self.evaluate_horizontal_c2iar(board) + self.evaluate_vertical_c2iar(board) + self.evaluate_diagonal_c2iar(board) + self.evaluate_downdiagonal_c2iar(board)
    
    def evaluate_horizontal_u2iar(self, board):
        m = len(board)
        n = len(board[0])
        total = 0
        for row in range(m):
            for col in range(n-2):
                if board[row,col] == self.player:
                    if board[row,col+1] == 0:
                        if board[row,col+2] == self.player:
                            total += self.C * self.w_u2iar
                        elif board[row,col+2] == 0:
                            if col < n - 3:
                                if board[row,col+3] == self.player:
                                    total += self.C * self.w_u2iar
                elif board[row,col] == self.opponent:
                    if board[row,col+1] == 0:
                        if board[row,col+2] == self.opponent:
                            total -= self.w_u2iar
                        elif board[row,col+2] == 0:
                            if col < n - 3:
                                if board[row,col+3] == self.opponent:
                                    total -= self.w_u2iar
        return total
        
    def evaluate_vertical_u2iar(self, board):
        m = len(board)
        n = len(board[0])
        total = 0
        for row in range(2,m):
            for col in range(n):
                if board[row,col] == self.player:
                    if board[row-1,col] == 0:
                        if board[row-2,col] == self.player:
                            total += self.C * self.w_u2iar
                        elif board[row-2,col] == 0:
                            if row >= 3:
                                if board[row-3,col] == self.player:
                                    total += self.C * self.w_u2iar
                elif board[row,col] == self.opponent:
                    if board[row-1,col] == 0:
                        if board[row-2,col] == self.opponent:
                            total -= self.w_u2iar
                        elif board[row-2,col] == 0:
                            if row >= 3:
                                if board[row-3,col] == self.opponent:
                                    total -= self.w_u2iar
        return total
                        
    def evaluate_diagonal_u2iar(self, board):
        m = len(board)
        n = len(board[0])
        total = 0
        for row in range(2,m):
            for col in range(n-2):
                if board[row,col] == self.player:
                    if board[row-1,col+1] == 0:
                        if board[row-2,col+2] == self.player:
                            total += self.C * self.w_u2iar
                        elif board[row-2,col+2] == 0:
                            if row >= 3 and col < n-3:
                                if board[row-3,col+3] == self.player:
                                    total += self.C * self.w_u2iar
                elif board[row,col] == self.opponent:
                    if board[row-1,col+1] == 0:
                        if board[row-2,col+2] == self.opponent:
                            total -= self.w_u2iar
                        elif board[row-2,col+2] == 0:
                            if row >= 3 and col < n-3:
                                if board[row-3,col] == self.opponent:
                                    total -= self.w_u2iar
        return total
                        
    def evaluate_downdiagonal_u2iar(self, board):
        m = len(board)
        n = len(board[0])
        total = 0
        for row in range(m-2):
            for col in range(n-2):
                if board[row,col] == self.player:
                    if board[row+1,col+1] == 0:
                        if board[row+2,col+2] == self.player:
                            total += self.C * self.w_u2iar
                        elif board[row+2,col+2] == 0:
                            if row < m-3 and col < n-3:
                                if board[row+3,col+3] == self.player:
                                    total += self.C * self.w_u2iar
                elif board[row,col] == self.opponent:
                    if board[row+1,col+1] == 0:
                        if board[row+2,col+2] == self.opponent:
                            total -= self.w_u2iar
                        elif board[row+2,col+2] == 0:
                            if row < m-3 and col < n-3:
                                if board[row-3,col] == self.opponent:
                                    total -= self.w_u2iar
        return total
                        
    def evaluate_u2iar(self, board):
        return self.evaluate_horizontal_u2iar(board) + self.evaluate_vertical_u2iar(board) + self.evaluate_diagonal_u2iar(board) + self.evaluate_downdiagonal_u2iar(board)
    
    def evaluate_horizontal_3iar(self, board):
        m = len(board)
        n = len(board[0])
        total = 0
        for row in range(m):
            for col in range(n-2):
                if board[row,col] == self.player:
                    if board[row,col+1] == self.player:
                        if board[row,col+2] == self.player:
                            total += self.C * self.w_3iar
                elif board[row,col] == self.opponent:
                    if board[row,col+1] == self.opponent:
                        if board[row,col+2] == self.opponent:
                            total -= self.w_3iar
        return total
        
    def evaluate_vertical_3iar(self, board):
        m = len(board)
        n = len(board[0])
        total = 0
        for row in range(2,m):
            for col in range(n):
                if board[row,col] == self.player:
                    if board[row-1,col] == self.player:
                        if board[row-2,col] == self.player:
                            total += self.C * self.w_3iar
                elif board[row,col] == self.opponent:
                    if board[row-1,col] == self.opponent:
                        if board[row-2,col] == self.opponent:
                            total -= self.w_3iar
        return total
                        
    def evaluate_diagonal_3iar(self, board):
        m = len(board)
        n = len(board[0])
        total = 0
        for row in range(2,m):
            for col in range(n-2):
                if board[row,col] == self.player:
                    if board[row-1,col+1] == self.player:
                        if board[row-2,col+2] == self.player:
                            total += self.C * self.w_3iar
                elif board[row,col] == self.opponent:
                    if board[row-1,col+1] == self.opponent:
                        if board[row-2,col+2] == self.opponent:
                            total -= self.w_3iar
        return total
                        
    def evaluate_downdiagonal_3iar(self, board):
        m = len(board)
        n = len(board[0])
        total = 0
        for row in range(m-2):
            for col in range(n-2):
                if board[row,col] == self.player:
                    if board[row+1,col+1] == self.player:
                        if board[row+2,col+2] == self.player:
                            total += self.C * self.w_3iar
                elif board[row,col] == self.opponent:
                    if board[row+1,col+1] == self.opponent:
                        if board[row+2,col+2] == self.opponent:
                            total -= self.w_3iar
        return total
                        
    def evaluate_3iar(self, board):
        return self.evaluate_horizontal_3iar(board) + self.evaluate_vertical_3iar(board) + self.evaluate_diagonal_3iar(board) + self.evaluate_downdiagonal_3iar(board)
    
    def evaluate_horizontal_4iar(self, board):
        m = len(board)
        n = len(board[0])
        total = 0
        for row in range(m):
            for col in range(n-3):
                if board[row,col] == self.player:
                    if board[row,col+1] == self.player:
                        if board[row,col+2] == self.player:
                            if board[row,col+3] == self.player:
                                total += self.C * self.w_4iar
                elif board[row,col] == self.opponent:
                    if board[row,col+1] == self.opponent:
                        if board[row,col+2] == self.opponent:
                            if board[row,col+3] == self.opponent:
                                total -= self.w_4iar
        return total
        
    def evaluate_vertical_4iar(self, board):
        m = len(board)
        n = len(board[0])
        total = 0
        for row in range(3,m):
            for col in range(n):
                if board[row,col] == self.player:
                    if board[row-1,col] == self.player:
                        if board[row-2,col] == self.player:
                            if board[row-3,col] == self.player:
                                total += self.C * self.w_4iar
                elif board[row,col] == self.opponent:
                    if board[row-1,col] == self.opponent:
                        if board[row-2,col] == self.opponent:
                            if board[row-3,col] == self.opponent:
                                total -= self.w_4iar
        return total
                        
    def evaluate_diagonal_4iar(self, board):
        m = len(board)
        n = len(board[0])
        total = 0
        for row in range(3,m):
            for col in range(n-3):
                if board[row,col] == self.player:
                    if board[row-1,col+1] == self.player:
                        if board[row-2,col+2] == self.player:
                            if board[row-3,col+3] == self.player:
                                total += self.C * self.w_4iar
                elif board[row,col] == self.opponent:
                    if board[row-1,col+1] == self.opponent:
                        if board[row-2,col+2] == self.opponent:
                            if board[row-3,col+3] == self.opponent:
                                total -= self.w_4iar
        return total
                        
    def evaluate_downdiagonal_4iar(self, board):
        m = len(board)
        n = len(board[0])
        total = 0
        for row in range(m-3):
            for col in range(n-3):
                if board[row,col] == self.player:
                    if board[row+1,col+1] == self.player:
                        if board[row+2,col+2] == self.player:
                            if board[row+3,col+3] == self.player:
                                total += self.C * self.w_4iar
                elif board[row,col] == self.opponent:
                    if board[row+1,col+1] == self.opponent:
                        if board[row+2,col+2] == self.opponent:
                            if board[row+3,col+3] == self.opponent:
                                total -= self.w_4iar
        return total
                        
    def evaluate_4iar(self, board):
        return self.evaluate_horizontal_4iar(board) + self.evaluate_vertical_4iar(board) + self.evaluate_diagonal_4iar(board) + self.evaluate_downdiagonal_4iar(board)
    
    def evaluate_center(self, board):
        m = len(board)
        n = len(board[0])
        total = 0
        for row in range(m):
            for col in range(n):
                if board[row,col] == self.player:
                    total += self.C * self.w_center / np.sqrt((row - (m-1)/2)**2 + (col - (n-1)/2)**2)
                elif board[row,col] == self.opponent:
                    total -= self.w_center / np.sqrt((row - (m-1)/2)**2 + (col - (n-1)/2)**2)
        return total
    
    def evaluate_pos(self, board):
        return self.evaluate_c2iar(board) + self.evaluate_u2iar(board) + self.evaluate_3iar(board) + self.evaluate_4iar(board) + self.evaluate_center(board)
    
    def simulate_board(self, board, move, opponents_move = False):
        adjusted_board = deepcopy(board)
        adjusted_board[move] = self.player if not opponents_move else self.opponent
        return adjusted_board
    
    def give_move(self, moves, board):
        current_move = moves[0]
        current_value = self.evaluate_pos(self.simulate_board(board, moves[0]))
        for move in moves[1:]:
            candidate_value = self.evaluate_pos(self.simulate_board(board, move))
            if candidate_value > current_value:
                current_move, current_value = move, candidate_value
        return current_move
            
        
class MyopicPlayer(BasicParameterPlayer):
    C = 2
    w_c2iar = 1
    w_u2iar = 1
    w_3iar = 10
    w_4iar = 100
    w_center = 1
    lapse_rate = 0.1
    
    def give_move(self, moves, board):
        if np.random.uniform() < self.lapse_rate:
            return moves[np.random.choice(len(moves))]
        else:
            current_move = moves[0]
            current_value = self.evaluate_pos(self.simulate_board(board, moves[0])) + np.random.normal()
            for move in moves[1:-1]:
                candidate_value = self.evaluate_pos(self.simulate_board(board, move))
                if candidate_value > current_value:
                    current_move, current_value = move, candidate_value
            return current_move

        
##############################
# Model from 2016/2017 paper #
##############################
        
class Node:
    def __init__(self, move = None, our_turn = True, value = -1000, children = []):
        self.move = move
        self.our_turn = our_turn
        self.value = value
        self.children = children
        
class TreeParameterPlayer(BasicParameterPlayer):
    C = 1.2
    w_c2iar = 1
    w_u2iar = 0.5
    w_3iar = 3.5
    w_4iar = 10
    w_center = 0.8
    pruning_threshold = 2
    stopping_probability = 1
    feature_drop_rate = 0.2
    lapse_rate = 0.05
    
    def evaluate_pos(self, board, features_used = [True, True, True, True, True]):
        value = 0
        if features_used[0]:
            value += self.evaluate_c2iar(board)
        if features_used[1]:
            value += self.evaluate_u2iar(board)
        if features_used[2]:
            value += self.evaluate_3iar(board)
        if features_used[3]:
            value += self.evaluate_4iar(board)
        if features_used[4]:
            value += self.evaluate_center(board)
        return value + np.random.normal()
    
    def select_node(self, tree):
        current_node = tree
        moves_to_get_here = []
        while len(current_node.children) > 0:
            child_values = [child.value for child in current_node.children]
            if current_node.our_turn:
                current_node = current_node.children[np.argmax(child_values)] #best child
            else:
                current_node = current_node.children[np.argmin(child_values)]
            moves_to_get_here.append(current_node.move)
        return current_node, moves_to_get_here
    
    def get_new_board_from_move_list(self, board, moves_to_get_here):
        new_board = deepcopy(board)
        parity = True
        for move in moves_to_get_here:
            new_board[move] = self.player if parity else self.opponent
            parity = not parity
        return new_board
    
    @staticmethod
    def get_moves_from_board(board):
        moves = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row,col] == 0:
                    moves.append((row,col))
        return moves
    
    @classmethod
    def prune_children(cls, node):
        child_values = [child.value for child in node.children]
        if node.our_turn:
            best_value = np.max(child_values)
            for child in node.children:
                if child.value < best_value - cls.pruning_threshold:
                    node.children.remove(child)
        else:
            best_value = np.min(child_values)
            for child in node.children:
                if child.value > best_value + cls.pruning_threshold:
                    node.children.remove(child)
    
    def expand_node(self, node, board, moves_to_get_here, features_used):
        new_board = self.get_new_board_from_move_list(board, moves_to_get_here)
        candidate_moves = self.get_moves_from_board(board)
        node.children = [Node(move, not node.our_turn, self.evaluate_pos(self.simulate_board(new_board, move, not node.our_turn), features_used)) for move in candidate_moves]
        #self.prune_children(node)        
    
    def backpropogate(self, node):
        for child in node.children:
            self.backpropogate(child)
        if len(node.children) > 0:
            if node.our_turn:
                node.value = np.max([child.value for child in node.children])
            else:
                node.value = np.min([child.value for child in node.children])
    
    def tree_search_iteration(self, tree, board, features_used):
        current_node, moves_to_get_here = self.select_node(tree)
        self.expand_node(current_node, board, moves_to_get_here, features_used)
        self.backpropogate(tree)
    
    def tree_search(self, moves, board):
        features_used = [True if np.random.uniform() > self.feature_drop_rate else False for _ in range(5)]
        tree = Node(value = self.evaluate_pos(board, features_used))
        self.tree_search_iteration(tree, board, features_used)
        while np.random.uniform() > self.stopping_probability:
            self.tree_search_iteration(tree, board, features_used)
            #print([child.value for child in tree.children])
        return tree.children[np.argmax([child.value for child in tree.children])].move
        
    def give_move(self, moves, board):
        if np.random.uniform() < self.lapse_rate:
            print("Lapsed")
            return moves[np.random.choice(len(moves))]
        else:
            return self.tree_search(moves, board)