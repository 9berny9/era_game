import itertools
import random


class Stone:
    """
    Each stone has four binary numbers.
    Each number is a specific characteristic of the stone. (shape, background, innerShape, innerColour)
    """
    def __init__(self, binary_list):
        self.binaryNumber = binary_list

        if binary_list[0] == 0:
            self.shape = 0
        else:
            self.shape = 1
        if binary_list[1] == 0:
            self.background = 0
        else:
            self.background = 1
        if binary_list[2] == 0:
            self.innerShape = 0
        else:
            self.innerShape = 1
        if binary_list[3] == 0:
            self.innerColour = 0
        else:
            self.innerColour = 1


class Player:
    def __init__(self, player_name):
        self.name = player_name
        self.winsNumber = 0

    def choose(self, desk_stones):
        """
        Function selects a stone for the second player from the available stones on the board.
        If the computer is playing, it selects a random stone from available list.
        """
        if self.name == "pc" or self.name == "pc1":
            self.choiceList = random.choice(desk_stones)
            self.choice = "".join(str(i) for i in self.choiceList)
            print(f"""{self.name} selects stone '{self.choice}' for enemy.""")
            return self.choiceList
        else:
            try:
                self.choice = input(f""""{self.name}, select a four digit stone number for enemy: """)
                self.choiceList = [int(i) for i in self.choice]
                while self.choiceList not in desk_stones:
                    self.choice = input(f"""Invalid choice.  {self.name}, choose available stone: """)
                    self.choiceList = [int(i) for i in self.choice]

                print(f"""{self.name} selects stone '{self.choice}' for enemy.""")
                return self.choiceList
            except:
                print("That's not a number!")

    def putStone(self, desk_fields):
        """
        Function selects field where the player places the stone.
        If the computer is playing, it selects a random field from available list.
        """
        if self.name == "pc" or self.name == "pc1":
            self.selectField = random.choice(desk_fields)
            print(f"""{self.name} placed a stone on the field: {self.selectField}""")
            return self.selectField
        else:
            try:
                self.selectField = int(input(f""""{self.name}, select field number for your stone: """))
                while self.selectField not in desk_fields:
                    self.selectField = int(input(f"""Invalid choice.  {self.name}, choose available field: """))

                print(f"""{self.name} placed a stone on the field: {self.selectField}""")
                return self.selectField
            except:
                print("That's not a number!")

    def checkWins(self, player_check_list, board):
        """
        Function over winning combinations and sets the object all available characteristics and looks for four of
        the same. If all winning combinations have already been used, the program will switch to True and print a draw.
        """
        # for cycle in characteristics
        for attr in ['shape', 'background', 'innerShape', 'innerColour']:
            # for cycle which gets a specific attribute of the object
            for a in [[getattr(j, attr) for j in i] for i in player_check_list]:
                # sum 0 or 4 means four identical characteristics side by side (player wins round)
                if sum(a) == 0 or sum(a) == 4:
                    print("=" * 32)
                    [print(i) for i in board]
                    print("=" * 60)
                    print(f"""{self.name} wins this round! These win stones has attribute: '{attr}'.""")
                    print("=" * 60)
                    self.winsNumber += 1
                    return True
        # players played all moves but no winners
        if len(player_check_list) == 10:
            print("=" * 32)
            [print(i) for i in board]
            print("=" * 32)
            print(f"""This round is a draw!""")
            print("=" * 32)
            return True
        # no move is victorious, so it continues
        else:
            return False


class GameDesk:
    """
    The game board has fields and stones that are gradually removed.
    """
    def __init__(self):
        self.board = [
            [' 11 ', ' 12 ', ' 13 ', ' 14 '],
            [' 21 ', ' 22 ', ' 23 ', ' 24 '],
            [' 31 ', ' 32 ', ' 33 ', ' 34 '],
            [' 41 ', ' 42 ', ' 43 ', ' 44 ']
        ]
        self.selected_stone = None
        self.stones = []
        self.fields = [11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34, 41, 42, 43, 44]
        self.makeAllStones()
        self.dictFieldsStones = {}

    def stonesCombinations(self):
        """
        Function returns all binary combination for stones in List of List.
        """
        stones_combinations = list(itertools.product([0, 1], repeat=4))
        return [list(i) for i in stones_combinations]

    def makeAllStones(self):
        """
        The function for each binary combination creates a stone and adds it to the GameDesk.
        """
        for i in self.stonesCombinations():
            self.stones.append(Stone(i))

    def stoneForPlayer(self, choice_list):
        """
        Function returns selected stone from the GameDesk.
        """
        self.selected_stone = [i for i in self.stones if i.binaryNumber == choice_list][0]

    def removeStone(self, choice_list):
        """
        Function removes stone from GameDesk.
        """
        self.stones = [i for i in self.stones if i.binaryNumber != choice_list]

    def removeField(self, choice_field):
        """
        Function removes field from GameDesk.
        """
        self.fields = [i for i in self.fields if i != choice_field]

    def replaceField(self, choice_field, put_stone):
        """
        Function adjusts game board for visualization.
        """
        number = str(choice_field)
        index = int(number[0]) - 1
        index_value = int(number[1]) - 1
        self.board[index][index_value] = put_stone

    def availableStones(self):
        """
        Function return stones that are still in game.
        """
        return [i.binaryNumber for i in self.stones]

    def availableFields(self):
        """
        Function return fields that are still in game.
        """
        return [i for i in self.fields]

    def dictFieldStone(self, field, stone):
        """
        Function creates a dictionary where the key is field and value is stone.
        """
        self.dictFieldsStones[field] = stone

    def checkPossibleComb(self, player_dict):
        """
        Function returns a list of possible winning combinations from currently played fields.
        """
        wins_comb = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34], [41, 42, 43, 44], [11, 21, 31, 41],
                     [12, 22, 32, 42], [13, 23, 33, 43], [14, 24, 34, 44], [11, 22, 33, 44], [14, 23, 32, 41]]
        check_all_list = []
        for i in wins_comb:
            check_list = []
            for b in i:
                if b in player_dict:
                    check_list.append(player_dict[b])
            if len(check_list) == 4:
                check_all_list.append(check_list)
        return check_all_list

    def deskDescription(self):
        """
        Function just for printing each round.
        """
        print(game.separator(32))
        [print(i) for i in self.board]
        print(game.separator(32))
        print("Stones available: ", self.availableStones())
        print("Fields available: ", self.fields)
        print(game.separator(60))


class GameRound:
    """
    The game round has endRound switcher and move for each turn.
    """
    def __init__(self, p1, p2, desk):
        self.endRound = False
        # switch on/off
        while not self.endRound:
            # move for player 1
            if self.move(p1, p2, desk) is True:
                break
            # move for player 2
            elif self.move(p2, p1, desk) is True:
                break

    def move(self, c1, c2, desk):
        """
        Function with other functions which evaluates the results of the move.
        """
        desk.deskDescription()
        c1.choose(desk.availableStones())
        desk.stoneForPlayer(c1.choiceList)
        desk.removeStone(c1.choiceList)
        c2.putStone(desk.availableFields())
        desk.removeField(c2.selectField)
        desk.dictFieldStone(c2.selectField, desk.selected_stone)
        desk.replaceField(c2.selectField, c1.choice)
        return c2.checkWins(desk.checkPossibleComb(desk.dictFieldsStones), desk.board)


class Game:
    """
    The game round has endRound switcher and move for each turn.
    """
    def __init__(self):
        self.endGame = False
        self.gameCounter = 0
        self.gameDesk = GameDesk()
        self.welcome_and_rules()
        self.firstPlayer = Player(input("First player name (for computer player 'pc'): "))
        self.secondPlayer = Player(input("Second player name (for computer player 'pc1'): "))

    def start(self):
        """
        Function checks if the game round is not over and ask for the next game.
        """
        while not self.endGame:
            GameRound(self.firstPlayer, self.secondPlayer, self.gameDesk)
            self.checkEndCondition()

    def checkEndCondition(self):
        """
        Function counts the rounds and asks for the next game. Each game starts with a different player.
        """
        self.gameCounter += 1
        print(f""" {self.firstPlayer.name}: {self.firstPlayer.winsNumber} wins, {self.secondPlayer.name}: {self.secondPlayer.winsNumber} wins""")
        answer = input("Play next game? y/n: ")
        if answer == 'y':
            print(self.separator(60))
            print('Watch out for the change of starting player')
            self.gameDesk = GameDesk()
            if self.gameCounter % 2 == 0:
                GameRound(self.firstPlayer, self.secondPlayer, self.gameDesk)
            else:
                GameRound(self.secondPlayer, self.firstPlayer, self.gameDesk)

            self.checkEndCondition()

        else:
            print(self.separator(60))
            print(f"""Game ended, {self.firstPlayer.name} has {self.firstPlayer.winsNumber} wins, and {self.secondPlayer.name} has {self.secondPlayer.winsNumber} wins""")
            self.determineWinner()
            print("See you next time!")
            print(self.separator(60))
            self.endGame = True

    def determineWinner(self):
        """
        Function for determine winner or draw.
        """
        result_string = "It's a Draw"
        if self.firstPlayer.winsNumber > self.secondPlayer.winsNumber:
            result_string = f"""Winner is {self.firstPlayer.name}"""
        elif self.firstPlayer.winsNumber < self.secondPlayer.winsNumber:
            result_string = f"""Winner is {self.secondPlayer.name}"""
        print(result_string)

    def welcome_and_rules(self):
        """
        Function returns description and rules of the game.
        """
        welcome = f"""
{self.separator(20)}
WELCOME TO ERA GAME!
{self.separator(20)}
ERA Game is turn-based strategy game between two players. 
There are 16 unique stones with 4 characteristics, which are placed into 4x4 board. 
All stones are visible to both players. 
Player, who completes four stones with at least one same characteristic in row, column or diagonal, is winner.
{self.separator(6)}
RULES:
{self.separator(6)}
Game begins by Player 1 choosing any stone from all 16 free stones. 
This chosen stone Player 1 gives to Player 2. Player 2 places the stone somewhere on the board.
Then Player 2 chooses any stone from 15 free stones and gives it to Player 1. Player 1 places stone somewhere on the board.
Winning row/column/diagonal is row of four stones with at least one same characteristic.
Both players take turns until all stones are placed or one of them wins.
{self.separator(12)}
GAME FIELD:
{self.separator(12)}
{self.gameDesk.board[0]}
{self.gameDesk.board[1]}
{self.gameDesk.board[2]}
{self.gameDesk.board[3]}
"""
        print(welcome)
        print(self.separator(46))
        input("Do you understand? Are you ready? Press enter: ")
        print(self.separator(46))

    def separator(self, delka=45):
        separator = delka * "="
        return separator


###### GAME PLAY ######
game = Game()
game.start()
