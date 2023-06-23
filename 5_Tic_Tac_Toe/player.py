import math
import random
class Player:
    def __init__(self, letter):
        #Letter is X or O
        self.letter = letter
        
    # We want all players to get their next move given a game
    def get_move(self, game):
        pass
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super()._init_letter()
        
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
       valid_square = False
       val = None
       while not valid_square:
           square = input(self.letter + '\'s turn. Input move (0-9): ')
           #Check that this is a correct value by trying to cast it into an integer.
           #If it is not an integer or not available on the board, it is invalid
           try:
               val = int(square)
               if val not in game.available_moves():
                   raise ValueError
               valid_square = True
        
    
