DIVIDER = '-' * 15


class PlayerBoard(object):

    """A PlayerBoard is the half of the board that a player controls

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

    def update(self, coordinate, value):
        self.board[coordinate] = value

    def output(self, flip):
        # Prints the current boardstate
        # Has an option for flipping the orientation for recessive player
        for x in 'ab':
            output = []
            for y in range(1, 9):
                output.append(str(self.board[x + str(y)]))

            if not flip:
                print(' '.join(output))
            else:
                print(' '.join(reversed(output)))


class GameBoard(object):

    """Both players' boards in one class

    Attributes:
        p1: PlayerBoard for player 1
        p2: PlayerBoard for player 2
    """

    def __init__(self):
        super(GameBoard, self).__init__()
        self.p1 = PlayerBoard()
        self.p2 = PlayerBoard()

    def getValue(self, player, coordinate):
        # Returns the stones in a players' specified square
        if player == 1:
            return self.p1.board[coordinate]
        else:
            return self.p2.board[coordinate]

    def subtract(self, player, coordinate, x):
        # Removes x stones from a players' square
        if player == 1:
            self.p1.update(coordinate, self.p1.board[coordinate] - x)
        else:
            self.p2.update(coordinate, self.p2.board[coordinate] - x)

    def pop(self, player, coordinate):
        # Returns the amount of stones in a players' square
        # Then removes them all
        if player == 1:
            temp = self.p1.board[coordinate]
            self.p1.update(coordinate, 0)
            return temp
        else:
            temp = self.p2.board[coordinate]
            self.p2.update(coordinate, 0)
            return temp

    def output(self, player):
        # Output both boards, depending on which player is currently dominant
        if player == 1:
            self.p2.output(True)
            print(DIVIDER)
            self.p1.output(False)
        else:
            self.p1.output(True)
            print(DIVIDER)
            self.p2.output(False)

    def playerCheck(self, player):
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
        if self.playerCheck(1):
            return 1
        elif self.playerCheck(2):
            return 2
        else:
            return False
