import numpy as np

from game import BeckGame
#from game import BeckGameCmd as BeckGame
#from game import BeckGameVisual as BeckGame
from nac_player import NACQlearnPlayer1, NACQlearnPlayer2, NACAlphaBetaPlayer

def main():
    players = [NACQlearnPlayer1, NACAlphaBetaPlayer]
    for i in range(10000):
        np.random.shuffle(players)
        player_one = players[0](player=1)
        player_two = players[1](player=2)
        game = BeckGame(player_one, player_two, (3,3,3))
        winner = game.play()
        if winner == 1:
            try:
                player_one.update_Q(1)
            except:
                player_two.update_Q(-1)
        elif winner == 2:
            try:
                player_one.update_Q(-1)
            except:
                player_two.update_Q(1)
        else:
            try:
                player_one.update_Q(0)
            except:
                player_two.update_Q(0)
        try:
            player_one.reset_game()
        except:
            player_two.reset_game()
        if i % 20 == 0:
            print(i)
    print("Done!")
    
if __name__ == '__main__':
    main()