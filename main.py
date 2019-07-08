import numpy as np

#from game import BeckGame
#from game import BeckGameCmd as BeckGame
from game import BeckGameVisual as BeckGame
#from human_player import Human
from human_player import HumanVisual as Human
from parameter_player import BasicParameterPlayer, MyopicPlayer, TreeParameterPlayer
from random_player import RandomPlayer
from nac_player import NACAlphaBetaPlayer

def main():
    players = [Human, NACAlphaBetaPlayer]
    np.random.shuffle(players)
    player_one = players[0](player=1)
    player_two = players[1](player=2)
    game = BeckGame(player_one, player_two, (3,3,3))
    game.play()
    input()
    
if __name__ == '__main__':
    main()