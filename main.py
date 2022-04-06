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
    def __init__(self, player_name):
        self.name = player_name
        self.winsNumber = 0


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
                return self.selectField

            except:
                print("That's not a number!")


    def checkWins(self, player_check_list, rounds_number, board):
        for attr in ['shape', 'background', 'innerShape', 'innerColour']:
            for win_stones in [[getattr(j, attr) for j in i] for i in player_check_list]:
                if sum(win_stones) == 0 or sum(win_stones) == 4:
                    [print(i) for i in board]
                    print(f"""{self.name} wins this round! These win stones has attribute: '{attr}'.""")
                    self.winsNumber += 1
                    return True
                elif rounds_number == 8:
                    [print(i) for i in board]
                    print(f"""This round is a draw!""")
                    return True
        return False


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

    def deskDescription(self):
        print("")
        [print(i) for i in self.board]
        print("")
        print(self.availableStones())
        print(self.fields)
        print("")

class GameRound:
    def __init__(self, p1, p2, desk):
        self.endRound = False
        self.roundCounter = 0

        while not self.endRound:
            desk.deskDescription()

            p1.choose(desk.availableStones())
            desk.stoneForPlayer(p1.choiceList)
            desk.removeStone(p1.choiceList)
            p2.putStone(desk.fields)
            desk.removeField(p2.selectField)
            desk.dictFieldStone(p2.selectField, desk.choice_stone)
            desk.replaceField(p2.selectField, p1.choice)
            self.endRound = p2.checkWins(desk.checkPossibleComb(desk.dictFieldsStones), self.roundCounter, desk.board)

            desk.deskDescription()
            p2.choose(desk.availableStones())
            desk.stoneForPlayer(p2.choiceList)
            desk.removeStone(p2.choiceList)
            p1.putStone(desk.fields)
            desk.removeField(p1.selectField)
            desk.dictFieldStone(p1.selectField, desk.choice_stone)
            desk.replaceField(p1.selectField, p2.choice)
            self.roundCounter += 1
            self.endRound = p1.checkWins(desk.checkPossibleComb(desk.dictFieldsStones), self.roundCounter, desk.board)

class Game:
    def __init__(self):
        self.endGame = False
        self.gameCounter = 0
        self.firstPlayer = Player(input("First player name: "))
        self.secondPlayer = Player(input("Second player name: "))
        self.gameDesk = GameDesk()

    def start(self):
        while not self.endGame:
            GameRound(self.firstPlayer, self.secondPlayer, self.gameDesk)
            self.checkEndCondition()

    def checkEndCondition(self):
        self.gameCounter += 1
        answer = input("Play next game? y/n: ")
        if answer == 'y':
            print('Watch out for the change of starting player')
            self.gameDesk = GameDesk()
            if self.gameCounter % 2 == 0:
                GameRound(self.firstPlayer, self.secondPlayer, self.gameDesk)
            else:
                GameRound(self.secondPlayer, self.firstPlayer, self.gameDesk)

            self.checkEndCondition()

        else:
            print(f"""Game ended, {self.firstPlayer.name} has {self.firstPlayer.winsNumber} wins, and {self.secondPlayer.name} has {self.secondPlayer.winsNumber} wins""")
            self.determineWinner()
            self.endGame = True

    def determineWinner(self):
        result_string = "It's a Draw"
        if self.firstPlayer.winsNumber > self.secondPlayer.winsNumber:
            result_string = f"""Winner is {self.firstPlayer.name}"""
        elif self.firstPlayer.winsNumber < self.secondPlayer.winsNumber:
            result_string = f"""Winner is {self.secondPlayer.name}"""
        print(result_string)




game = Game()
game.start()






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
