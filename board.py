DIVIDER = '-' * 15


class PlayerBoard(object):

    """
    A PlayerBoard is the half of the board that a player controls

    Attributes:
        board: a dict of the board that the player controls
            key: tuple(x, y)
            x: 'a' or 'b', representative of row
            y: int of 1-8, representative of column
            There is no inbuilt error checking: input must be sanitized
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
        # Has an option for flipping the orientation for recessive player
        if not flip:
            ordering = 'ab'
        else:
            ordering = 'ba'

        for row in ordering:
            output = [self.board[row + str(col)] for col in range(1, 9)]

            if not flip:
                print(' '.join([str(i) for i in output]))
            else:
                print(' '.join([str(i) for i in reversed(output)]))


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
        else:
            return self.p2.board[coord]

    def increment(self, player, coord, x):
        # Removes x stones from a players' square
        if player == 1:
            self.p1.update(coord, self.getValue(1, coord) + x)
        else:
            self.p2.update(coord, self.getValue(2, coord) + x)

    def pop(self, player, coord):
        # Returns the amount of stones in a players' square
        # Then removes them all
        if player == 1:
            temp = self.getValue(1, coord)
            self.p1.update(coord, 0)
            return temp
        else:
            temp = self.getValue(2, coord)
            self.p2.update(coord, 0)
            return temp

    def output(self, player):
        # Output a board, depending on which player is specified
        if player == 1:
            self.p2.output(True)
            print(DIVIDER)
            self.p1.output(False)
        else:
            self.p1.output(True)
            print(DIVIDER)
            self.p2.output(False)

    def _playerCheck(self, player):
        if player == 1:
            for i in self.p1.board.items():
                if i != 0:
                    return False
            return 1
        else:
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
