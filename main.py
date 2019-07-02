#from game import BeckGame
#from game import BeckGameCmd as BeckGame
from game import BeckGameVisual as BeckGame
#from human_player import Human
from human_player import HumanVisual as Human

def main():
    player_one = Human()
    player_two = Human()
    game = BeckGame(player_one, player_two)
    game.play()
    
if __name__ == '__main__':
    main()