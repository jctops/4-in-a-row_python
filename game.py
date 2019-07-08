import numpy as np
import sys
import pygame

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
            [self.board[pos[0]+i, pos[1]+i] for i in range(self.k)]
        )
    
    def check_win_downleft(self, pos):
        return self.check_array_elements_same(
            [self.board[pos[0]+i, pos[1]-i] for i in range(self.k)]
        )
    
    def check_win_up(self, pos):
        return self.check_array_elements_same(self.board[pos[0]-self.k+1:pos[0]+1, pos[1]])
    
    def check_win_upright(self, pos):
        return self.check_array_elements_same(
            [self.board[pos[0]-i, pos[1]+i] for i in range(self.k)]
        )
    
    def check_win_upleft(self, pos):
        return self.check_array_elements_same(
            [self.board[pos[0]-i, pos[1]-i] for i in range(self.k)]
        )
    
    def check_win_right(self, pos):
        return self.check_array_elements_same(self.board[pos[0], pos[1]:pos[1]+self.k])
    
    def check_win_left(self, pos):
        return self.check_array_elements_same(self.board[pos[0], pos[1]-self.k+1:pos[1]+1])
    '''  
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
        return won, -1'''
    
    def check_win(self, pos):
        won = False
        
        possible_downs = [(pos[0]-i, pos[1]) for i in range(self.k) if pos[0]>=i and pos[0]-i+self.k<=self.m]
        for _pos in possible_downs:
            won = won or self.check_win_down(_pos)
            
        possible_rights = [(pos[0], pos[1]-i) for i in range(self.k) if pos[1]>=i and pos[1]-i+self.k<=self.n]
        for _pos in possible_rights:
            won = won or self.check_win_right(_pos)
            
        possible_downrights = [(pos[0]-i, pos[1]-i) for i in range(self.k) if pos[0]>=i and pos[0]-i+self.k<=self.m and pos[1]>=i and pos[1]-i+self.k<=self.n]
        for _pos in possible_downrights:
            won = won or self.check_win_downright(_pos)
            
        possible_uprights = [(pos[0]+i, pos[1]-i) for i in range(self.k) if pos[0]+i+1>=self.k and pos[0]+i<self.m and pos[1]>=i and pos[1]-i+self.k<=self.n]
        for _pos in possible_uprights:
            won = won or self.check_win_upright(_pos)
            
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
            if self.player_one_turn:
                pos = self.player_one.give_move(self.moves, self.board)
            else:
                pos = self.player_two.give_move(self.moves, self.board)
            self.execute_move(pos)
            turns += 1
        if self.winner == 1:
            print("Player one wins!")
        elif self.winner == 2:
            print("Player two wins!")
        else:
            print("Draw - good game!")
        return self.winner
        
class BeckGameCmd(BeckGame):
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

class BeckGameVisual(BeckGame): 
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    DARK_BROWN = (222, 184, 135)
    LIGHT_BROWN = (255, 248, 220)
    SQUARESIZE = 100
    RADIUS = int(SQUARESIZE/2 - 5)
    
    def __init__(self, player_one, player_two, beckdata = (4,9,4)):
        self.player_one = player_one
        self.player_two = player_two
        self.m, self.n, self.k = self.validate_beckdata(beckdata)
        self.board = np.zeros((self.m, self.n))
        self.player_one_turn = True
        self.gameover = False
        self.winner = -1
        self.moves = [(row, col) for row in range(0,self.m) for col in range(0,self.n)]
        
        self.height = self.SQUARESIZE * self.m
        self.width = self.SQUARESIZE * self.n
        self.size = (self.width, self.height)
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
    
    def draw_board(self):
        pygame.draw.rect(self.screen, self.DARK_BROWN, (0,0,self.width,self.height))
        for row in range(self.m):
            for col in range(self.n):
                colour = self.WHITE if self.board[row,col] == 1 else self.BLACK if self.board[row,col] == 2 else self.LIGHT_BROWN
                pygame.draw.circle(self.screen, colour, (int(col*self.SQUARESIZE+self.SQUARESIZE/2), int(row*self.SQUARESIZE+self.SQUARESIZE/2)), self.RADIUS)
        pygame.display.update()
    
    def play(self):
        turns = 0
        while turns < self.m*self.n and not self.gameover:
            self.draw_board()
            if self.player_one_turn:
                pos = self.player_one.give_move(self.moves, self.board)
            else:
                pos = self.player_two.give_move(self.moves, self.board)
            self.execute_move(pos)
            turns += 1
        if self.winner == 1:
            print("Player one wins!")
        elif self.winner == 2:
            print("Player two wins!")
        else:
            print("Draw - good game!")
        self.draw_board()
        return self.winner
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()