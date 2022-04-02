import itertools

# 16 stones with four characteristic
available_stones = list(itertools.product([0,1], repeat = 4))



def main():
    '''
    The game running fuction.
    '''
    welcome_and_rules()

def welcome_and_rules():
    '''
    Function print welcome and rules for two players.
    '''
    welcome = f"""
WELCOME TO ERA GAME!
{separator(30)}
GAME DESCRIPTION:
ERA Game is turn-based strategy game between two players. 
There are 16 unique stones with 4 characteristics, which are placed into 4x4 board. 
All stones are visible to both players. 
Player, who completes four stones with at least one same characteristic in row, column or diagonal, is winner.
{separator(30)}
RULES:
Game begins by Player 1 choosing any stone from all 16 free stones. 
This chosen stone Player 1 gives to Player 2. Player 2 places the stone somewhere on the board.
Then Player 2 chooses any stone from 15 free stones and gives it to Player 1. Player 1 places stone somewhere on the board.
Winning row/column/diagonal is row of four stones with at least one same characteristic.
Both players take turns until all stones are placed or one of them wins.
{separator(30)}
GAME FIELD:
{game_board()}


{separator(30)}
Let's start the game!
{separator(30)}"""

    return print(welcome)

def separator(delka=45):
    """
    Description:
    Function create separator with '=' with length input number
    Sample:
    separator(5)
    Result:
    =====
    """
    separator = delka * "="
    return separator

def number_to_list(number):
    number_choice = []
    for i in str(number):
        number_choice.append(int(i))
    return number_choice

class Stone:
    def __init__(self, characteristic):
        self.characteristic = characteristic

        if characteristic[3] == 0:
            self.name_inner_shape = 'Inner Square'
        else:
            self.name_inner_shape = 'Inner Circle'
        if characteristic[2] == 0:
            self.name_inner_colour = 'Red'
        else:
            self.name_inner_colour = 'Blue'
        if characteristic[1] == 0:
            self.name_shape = 'Square'
        else:
            self.name_shape = 'Circle'
        if characteristic[0] == 0:
            self.name_background = 'White'
        else:
            self.name_background = 'Black'

        self.name = (self.name_background + ' ' + self.name_shape + ' ' + self.name_inner_colour + ' ' + self.name_inner_shape)

def game_board():
    game_board = """+----+----+----+----+
| 11 | 12 | 13 | 14 |
+----+----+----+----+
| 21 | 22 | 23 | 24 |
+----+----+----+----+
| 31 | 32 | 33 | 34 |
+----+----+----+----+
| 41 | 42 | 43 | 44 |
+----+----+----+----+"""
    return game_board

