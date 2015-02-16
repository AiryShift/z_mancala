# Allows board to be imported
import sys
sys.path.insert(0, '../')
import board
import re
from collections import Counter

ASSOCIATIONS = {str(k): str(v) for k, v in
                zip(range(1, 9), reversed(range(1, 9)))}

STANDARD_ORDER = []
for y in reversed(range(1, 9)):
    STANDARD_ORDER.append('a' + str(y))
for y in range(1, 9):
    STANDARD_ORDER.append('b' + str(y))


def nextTurn(curTurn):
    if curTurn == 1:
        return 2
    else:
        return 1


def legitimate(move, player, checks=None):
    if not re.match(r'^[ab][1-9]$', move):
        return False
    if checks:
        if move not in checks:
            return False
    return True


def getMove(checks=None):
    move = input("Player {name}, enter a move: "
                 .format(name=playerTurn))
    while not legitimate(move, playerTurn, checks):
        print('Move was not legitimate.')
        move = input("Player {name}'s turn. Enter a move: "
                     .format(name=playerTurn))
    print()
    return move


def nextPos(coord):
    firstChar, secondChar = coord
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


def resow(coord, opponentStones):
    location = STANDARD_ORDER.index(coord)
    for i in STANDARD_ORDER[location:] + STANDARD_ORDER[:location]:
        if game.getValue(playerTurn, i) == 0:  # Looking for empty hole
            emptyHole = i
            break
    else:  # Nobreak: no empty hole
        highestValue = max(game.values(playerTurn))

        if Counter(game.values(playerTurn))[highestValue] > 1:  # Choose one
            choices = []
            for i in STANDARD_ORDER:
                if game.getValue(playerTurn, i) == highestValue:
                    choices.append(i)

            print('Possible choices:')
            for i in choices:
                print(i)

            makeMove(move=getMove(), hand=opponentStones)
            return
        else:  # Resow from the highestValue
            makeMove(move=game.index(highestValue), hand=opponentStones)
            return
    # First empty hole
    makeMove(move=emptyHole, hand=opponentStones)


def captureStones(move):
    firstChar, secondChar = move
    if firstChar == 'a':
        y = ASSOCIATIONS[secondChar]
        opponentCoords = [x + y for x in 'ab']

        if int(opponentCoords[0][1]) > 0:  # If opponent's 'a' row has a stone
            opponentStones = 0
            for coord in opponentCoords:
                opponentStones += game.pop(nextTurn(playerTurn), coord)
            resow(move, opponentStones)


def makeMove(move, hand=0):
    if not hand:
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

    makeMove(getMove())

    turnNumber += 1
    playerTurn = nextTurn(playerTurn)

print('Player {playerName} wins!'
      .format(playerName=game.done()))
