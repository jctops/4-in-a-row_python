import numpy as np
from human_player import Human

class BeckGame:
    def __init__(self, player_one, player_two, beckdata = (4,9,4)):
        self.player_one = player_one
        self.player_two = player_two
        self.m, self.n, self.k = self.validate_beckdata(beckdata)
        self.board = np.zeros((self.m, self.n))
        self.player_one_turn = True
        self.gameover = False
        self.winner = -1
        self.moves = [(row, col) for row in range(0,self.m) for col in range(0,self.n)]
    
    @staticmethod
    def validate_beckdata(beckdata):
        assert isinstance(beckdata, tuple), "Inputted Beck data is not a tuple: {0}".format(beckdata)
        assert len(beckdata) == 3, "Inputted Beck data does not have exactly 3 values: {0}".format(beckdata)
        assert isinstance(beckdata[0], int), "m is not an integer: {0}".format(beckdata[0])
        assert isinstance(beckdata[1], int), "n is not an integer: {0}".format(beckdata[1])
        assert isinstance(beckdata[2], int), "k is not an integer: {0}".format(beckdata[2])
        return beckdata

    def receive_move(self, player):
        pass
    
    @staticmethod
    def check_array_elements_same(arr):
        return np.all(arr == arr[0])
    
    def check_win_down(self, pos):
        return self.check_array_elements_same(self.board[pos[0]:pos[0]+self.k, pos[1]])
    
    def check_win_downright(self, pos):
        return self.check_array_elements_same(
            [self.board[pos[0], pos[1]],
             self.board[pos[0]+1, pos[1]+1],
             self.board[pos[0]+2, pos[1]+2],
             self.board[pos[0]+3, pos[1]+3]
            ]
        )
    
    def check_win_downleft(self, pos):
        return self.check_array_elements_same(
            [self.board[pos[0], pos[1]],
             self.board[pos[0]+1, pos[1]-1],
             self.board[pos[0]+2, pos[1]-2],
             self.board[pos[0]+3, pos[1]-3]
            ]
        )
    
    def check_win_up(self, pos):
        return self.check_array_elements_same(self.board[pos[0]-self.k+1:pos[0]+1, pos[1]])
    
    def check_win_upright(self, pos):
        return self.check_array_elements_same(
            [self.board[pos[0], pos[1]],
             self.board[pos[0]-1, pos[1]+1],
             self.board[pos[0]-2, pos[1]+2],
             self.board[pos[0]-3, pos[1]+3]
            ]
        )
    
    def check_win_upleft(self, pos):
        return self.check_array_elements_same(
            [self.board[pos[0], pos[1]],
             self.board[pos[0]-1, pos[1]-1],
             self.board[pos[0]-2, pos[1]-2],
             self.board[pos[0]-3, pos[1]-3]
            ]
        )
    
    def check_win_right(self, pos):
        return self.check_array_elements_same(self.board[pos[0], pos[1]:pos[1]+self.k])
    
    def check_win_left(self, pos):
        return self.check_array_elements_same(self.board[pos[0], pos[1]-self.k+1:pos[1]+1])
    
    def check_win(self, pos):
        won = False
        if pos[0] <= self.m - self.k:
            won = self.check_win_down(pos)
            if pos[1] <= self.n - self.k:
                won = won or self.check_win_downright(pos)
            if pos[1] >= self.k - 1:
                won = won or self.check_win_downleft(pos)
        if pos[0] >= self.k - 1:
            won = self.check_win_up(pos)
            if pos[1] <= self.n - self.k:
                won = won or self.check_win_upright(pos)
            if pos[1] >= self.k - 1:
                won = won or self.check_win_upleft(pos)
        if pos[1] <= self.n - self.k:
            won = won or self.check_win_right(pos)
        if pos[1] >= self.k - 1:
            won = won or self.check_win_left(pos)
        if won:
            return won, 1 if self.player_one_turn else 2
        return won, -1
    
    def execute_move(self, pos):
        assert self.board[pos] == 0, "Position is not available: {0}".format(pos)
        if self.player_one_turn:
            self.board[pos] = 1
        else:
            self.board[pos] = 2
        self.gameover, self.winner = self.check_win(pos)
        self.player_one_turn = not self.player_one_turn
        self.moves.remove(pos)
        
    def play(self):
        turns = 0
        while turns < self.m*self.n and not self.gameover:
            print(self.board)
            if self.player_one_turn:
                pos = self.player_one.give_move(self.moves)
            else:
                pos = self.player_two.give_move(self.moves)
            self.execute_move(pos)
            turns += 1
        if self.winner == 1:
            print("Player one wins!")
        elif self.winner == 2:
            print("Player two wins!")
        else:
            print("Draw - good game!")
        print(self.board)