# Allows board to be imported
import sys
sys.path.insert(0, '../')

import board
ASSOCIATIONS = dict(
    zip(
        map(str, range(1, 9)), map(str, reversed(range(1, 9)))))


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


def getMove():
    move = input("Player {name}'s turn. Enter a move: "
                 .format(name=playerTurn))
    while not legitimate(move, playerTurn):
        print('Move was not legitimate.')
        move = input("Player {name}'s turn. Enter a move: "
                     .format(name=playerTurn))
    print()
    return move


def nextPos(coordinate):
    firstChar, secondChar = coordinate
    if firstChar == 'a':
        if secondChar == '1':
            firstChar, secondChar = 'b', '1'
        else:
            secondChar = str(int(secondChar) - 1)
    else:  # firstChar == 'b'
        if secondChar == '8':
            firstChar, secondChar = 'a', '8'
        else:
            secondChar = str(int(secondChar) + 1)
    return firstChar + secondChar


def nextTurn(curTurn):
    if curTurn == 1:
        return 2
    else:
        return 1


def captureStones(move):
    firstChar, secondChar = move
    if firstChar == 'a':
        y = ASSOCIATIONS[secondChar]
        opponentCoords = [x + y for x in 'ab']

        if int(opponentCoords[0][1]) > 0:  # If opponent's 'a' row has a stone
            for coordinate in opponentCoords:
                game.pop(nextTurn(playerTurn), coordinate)


def makeMove(move):
    hand = game.pop(playerTurn, move)

    while hand > 0:
        move = nextPos(move)
        game.increment(playerTurn, move, 1)
        hand -= 1

    if game.getValue(playerTurn, move) != 1:
        makeMove(move)
    else:
        captureStones(move)


game = board.GameBoard()
turnNumber = 1
playerTurn = 1

while not game.done():
    print('Turn {num}'
          .format(num=turnNumber))
    game.output(playerTurn)

    move = getMove()
    makeMove(move)

    turnNumber += 1
    playerTurn = nextTurn(playerTurn)

print('Player {playerName} wins!'
      .format(playerName=game.done()))
