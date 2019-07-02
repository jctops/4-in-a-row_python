from game import BeckGame
from human_player import Human

def main():
    player_one = Human()
    player_two = Human()
    game = BeckGame(player_one, player_two)
    game.play()
    
if __name__ == '__main__':
    main()