import itertools


class Stone:
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
    def __init__(self):
        self.name = input("Your name: ")
        self.movesNumber = 0
        self.winsNumber = 0
        self.drawsNumber = 0

    def choose(self, desk_stones):
        while True:
            try:
                self.choice = input(f""""{self.name}, select a four digit stone number for enemy: """)
                self.choiceList = [int(i) for i in self.choice]
                while self.choiceList not in desk_stones:
                    self.choice = input(f"""Invalid choice.  {self.name}, choose available stone: """)
                    self.choiceList = [int(i) for i in self.choice]

                print(f"""{self.name} selects stone: {self.choice}""")
                return self.choiceList
            except:
                print("That's not a number!")

    def putStone(self, desk_fields):
        while True:
            try:
                self.selectField = int(input(f""""{self.name}, select field number for your stone: """))
                while self.selectField not in desk_fields:
                    self.selectField = int(input(f"""Invalid choice.  {self.name}, choose available field: """))

                print(f"""{self.name} selects field: {self.selectField}""")
                self.movesNumber += 1

                return self.selectField
            except:
                print("That's not a number!")


    def checkWins(self, player_check_list):
        for attr in ['shape', 'background', 'innerShape', 'innerColour']:
            for win_stones in [[getattr(j, attr) for j in i] for i in player_check_list]:
                if sum(win_stones) == 0 or sum(win_stones) == 4:
                    print(f'''win: {self.name}''', win_stones)

class GameDesk:
    def __init__(self):
        self.board = [
            [' 11 ', ' 12 ', ' 13 ', ' 14 '],
            [' 21 ', ' 22 ', ' 23 ', ' 24 '],
            [' 31 ', ' 32 ', ' 33 ', ' 34 '],
            [' 41 ', ' 42 ', ' 43 ', ' 44 ']
        ]
        self.stones = []
        self.fields = [11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34, 41, 42, 43, 44]
        self.makeAllStones()
        self.dictFieldsStones = {}

    def stonesCombinations(self):
        # all binanry cobinations for stones
        stones_combinations = list(itertools.product([0, 1], repeat=4))
        # convert list with tuples to list with lists
        return [list(i) for i in stones_combinations]

    def makeAllStones(self):
        for i in self.stonesCombinations():
            self.stones.append(Stone(i))

    def stoneForPlayer(self, choice_list):
        self.choice_stone = [i for i in self.stones if i.binaryNumber == choice_list][0]

    def removeStone(self, choice_list):
        self.stones = [i for i in self.stones if i.binaryNumber != choice_list]

    def removeField(self, choice_field):
        self.fields = [i for i in self.fields if i != choice_field]

    def replaceField(self, choice_field, put_stone):
        number = str(choice_field)
        index = int(number[0]) - 1
        index_value = int(number[1]) - 1
        self.board[index][index_value] = put_stone

    def availableStones(self):
        return [i.binaryNumber for i in self.stones]

    def availableFields(self):
        return [i for i in self.fields]

    def dictFieldStone(self, field, stone):
        self.dictFieldsStones[field] = stone

    def checkPossibleComb(self, player_dict):
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

    def roundDescription(self):
        print("")
        [print(i) for i in self.board]
        print("")
        print(self.availableStones())
        print(self.fields)
        print("")

class GameRound:
    def __init__(self, p1, p2, desk):
        self.endRound = True
        self.roundCounter = 0

        desk.roundDescription()
        p1.choose(desk.availableStones())
        desk.stoneForPlayer(p1.choiceList)
        desk.removeStone(p1.choiceList)
        p2.putStone(desk.fields)
        desk.removeField(p2.selectField)
        desk.dictFieldStone(p2.selectField, desk.choice_stone)
        desk.replaceField(p2.selectField, p1.choice)
        p2.checkWins(desk.checkPossibleComb(desk.dictFieldsStones))

        desk.roundDescription()
        p2.choose(desk.availableStones())
        desk.stoneForPlayer(p2.choiceList)
        desk.removeStone(p2.choiceList)
        p1.putStone(desk.fields)
        desk.removeField(p1.selectField)
        desk.dictFieldStone(p1.selectField, desk.choice_stone)
        desk.replaceField(p1.selectField, p2.choice)
        p1.checkWins(desk.checkPossibleComb(desk.dictFieldsStones))


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
            GameRound(self.firstPlayer, self.secondPlayer, self.gameDesk)
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
