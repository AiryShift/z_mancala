import sys
sys.path.insert(0, '../')
import board
ASSOCIATIONS = dict(
    zip(
        range(1, 9), reversed(range(1, 9))))


def legitimate(move, player):
    if len(move) != 2:
        return False

    firstChar, secondChar = move

    if firstChar not in 'ab':
        return False

    if not secondChar.isnumeric():
        return False

    if int(secondChar) not in range(1, 9):
        return False

    if game.getValue(player, move) == 0:
        return False
    return True


def getMove(player):
    move = input("Player {playerName}'s turn. Enter a move: "
                 .format(playerName=player))
    while not legitimate(move, player):
        print('Move was not legitimate.')
        move = input("Player {playerName}'s turn. Enter a move: "
                     .format(playerName=player))
    print()
    return move


game = board.GameBoard()
turn = 1

while not game.done():
    print('Turn {turnNumber}'
          .format(turnNumber=turn))
    game.output(turn % 2)
    move = getMove(turn % 2)

    turn += 1

print('Player {playerName} wins!'
      .format(playerName=game.done()))
