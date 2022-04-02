import itertools

# 16 stones with four characteristic
all_stones = list(itertools.product([0,1], repeat = 4))



game_board = {

    "edit" : """
    +----+----+----+----+
    | 11 | 12 | 13 | 14 |
    +----+----+----+----+
    | 21 | 22 | 23 | 24 |
    +----+----+----+----+
    | 31 | 32 | 33 | 34 |
    +----+----+----+----+
    | 41 | 42 | 43 | 44 |
    +----+----+----+----+
    """
}