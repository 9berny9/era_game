import itertools


class Stone:
    def __init__(self,binary_list):

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
    def __init__(self):
        self.name = input("Your name: ")
        self.movesNumber = 0
        self.winsNumber = 0
        self.drawsNumber = 0
        self.playerStones = []
        self.choiceStone = []

    def choose(self):
        self.choice = input(f""""{self.name}, select stone number for enemy: """)
        print(f"""{self.name} selects: {self.choice}""")

    def addStoneToPlayer(self, choice):
        # hold only one choice
        self.choiceStone.clear()
        # convert string to list
        for i in choice:
            self.choiceStone.append(int(i))
        # add choice to list with all choices
        self.playerStones.append(list(self.choiceStone))
        return self.choiceStone


    def putStone(self):
        self.selectField = input(f""""{self.name}, select field number for your stone: """)
        self.movesNumber += 1


class GameDesk:

    def __init__(self):
        self.board = [[11, 12, 13, 14], [21, 22, 23, 24],  [31, 32, 33, 34], [41, 42, 43, 44]]
        self.stones = []
        self.makeAllStones()

    def stonesCombinations(self):
        # all binanry cobinations for stones
        stones_combinations = list(itertools.product([0, 1], repeat=4))
        # convert list with tuples to list with lists
        return [list(i) for i in stones_combinations]

    def makeAllStones(self):
        for i in self.stonesCombinations():
            self.stones.append(Stone(i))

    def removeStone(self, choice_list):
        self.stones = [i for i in self.stones if i.binaryNumber != choice_list]

    def availableStones(self):
        return [i.binaryNumber for i in self.stones]

class GameRound:
    def __init__(self, p1, p2, desk):
        self.endRound = True
        self.roundCounter = 0


        # show available stones
        print(desk.availableStones())
        p1.choose()

        p2.addStoneToPlayer(p1.choice)
        desk.removeStone(p2.choiceStone)
        p2.putStone()

        print(desk.availableStones())
        p2.choose()

        p1.addStoneToPlayer(p2.choice)
        desk.removeStone(p1.choiceStone)
        p1.putStone()


class Game:
    def __init__(self):
        self.endGame = False
        self.firstPlayer = Player()
        self.secondPlayer = Player()
        self.gameDesk = GameDesk()

    def start(self):
        while not self.endGame:
            game_round = GameRound(self.firstPlayer, self.secondPlayer, self.gameDesk)
            while not game_round.endRound:
                self.checkEndCondition()

    def checkEndCondition(self):
        answer = input("Play next game? y/n: ")
        if answer == 'y':
            GameRound(self.firstPlayer, self.secondPlayer)
            self.checkEndCondition()
        else:
            print(
                "Game ended, {p1name} has {p1wins}, and {p2name} has {p2wins}".format(p1name=self.firstPlayer.name,
                                                                                          p1wins=self.firstPlayer.winsNumber,
                                                                                          p2name=self.secondPlayer.name,
                                                                                          p2wins=self.secondPlayer.winsNumber))
            self.determineWinner()
            self.endGame = True

    def determineWinner(self):
        resultString = "It's a Draw"
        if self.firstPlayer.winsNumber > self.secondPlayer.winsNumber:
            resultString = "Winner is {name}".format(name=self.firstPlayer.name)
        elif self.firstPlayer.winsNumber < self.secondPlayer.winsNumber:
            resultString = "Winner is {name}".format(name=self.secondPlayer.name)

        print(resultString)

game = Game()
game.start()



####### DOESNT WORK NOW




def check_columns(board):
    for column in board:
        if len(set(column)) == 1 and column[0] is not None:
            return column[0]

def check_rows(board):
    return check_columns(zip(*reversed(board)))  # rotate the board 90 degrees

def compareChoice(self, p1, p2):
    return
######
##########################################
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






