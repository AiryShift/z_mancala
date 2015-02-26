DIVIDER = '-' * 15
ORDER = [[x + str(y) for y in range(1, 9)] for x in 'ab']
REVERSE_ORDER = [[x + str(y) for y in reversed(range(1, 9))] for x in 'ba']


class PlayerBoard(object):

    """
    A PlayerBoard is the half of the board that a player controls

    Attributes:
        board: a dict of the board that the player controls
            key: str(x) + str(y)
                x: 'a' or 'b', representative of row
                y: int of 1-8, representative of column
    """

    def __init__(self):
        super(PlayerBoard, self).__init__()
        self.board = {}
        for x in 'ab':
            for y in range(1, 9):
                self.board[x + str(y)] = 2

    def update(self, coord, value):
        self.board[coord] = value

    def output(self, flip):
        # Prints the current boardstate
        # Has an option for flipping the orientation for non-dominant player
        if not flip:
            for row in ORDER:
                print(' '.join([str(self.board[i]) for i in row]))
        else:
            for row in REVERSE_ORDER:
                print(' '.join([str(self.board[i]) for i in row]))


class GameBoard(object):

    """
    Both players' boards in one class

    Attributes:
        p1: PlayerBoard for player 1
        p2: PlayerBoard for player 2
    """

    def __init__(self):
        super(GameBoard, self).__init__()
        self.p1 = PlayerBoard()
        self.p2 = PlayerBoard()

    def getValue(self, player, coord):
        # Returns the stones in a players' specified square
        if player == 1:
            return self.p1.board[coord]
        else:  # player == 2
            return self.p2.board[coord]

    def values(self, player):
        if player == 1:
            return self.p1.values()
        else:  # player == 2
            return self.p2.values()

    def index(self, player, stones):
        if player == 1:
            for k, v in self.p1.items():
                if v == stones:
                    return k
            return 0
        else:  # player == 2
            for k, v in self.p2.items():
                if v == stones:
                    return k
            return 0

    def increment(self, player, coord, x):
        # Removes x stones from a players' square
        if player == 1:
            self.p1.update(coord, self.getValue(1, coord) + x)
        else:  # player == 2
            self.p2.update(coord, self.getValue(2, coord) + x)

    def pop(self, player, coord):
        # Returns the amount of stones in a players' square
        # Then removes them all
        if player == 1:
            temp = self.getValue(1, coord)
            self.p1.update(coord, 0)
            return temp
        else:  # player == 2
            temp = self.getValue(2, coord)
            self.p2.update(coord, 0)
            return temp

    def output(self, player):
        # Output a board, depending on which player is specified
        if player == 1:
            self.p2.output(True)
            print(DIVIDER)
            self.p1.output(False)
        else:  # player == 2
            self.p1.output(True)
            print(DIVIDER)
            self.p2.output(False)

    def _playerCheck(self, player):
        if player == 1:
            for i in self.p1.board.items():
                if i != 0:
                    return False
            return 1
        else:  # player == 2
            for i in self.p2.board.items():
                if i != 0:
                    return False
            return 2

    def done(self):
        if self._playerCheck(1):
            return 1
        elif self._playerCheck(2):
            return 2
        else:
            return False
