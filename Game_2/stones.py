# Allows board to be imported
import sys
sys.path.insert(0, '../')

import board
from collections import Counter

ASSOCIATIONS = dict(
    zip(
        map(str, range(1, 9)),
        map(str, reversed(range(1, 9)))))
ORDER = ['a' + str(y) for y in reversed(range(1, 9))] + ['b' + str(y) for y in range(1, 9)]


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


def getMove(moveType):
    if moveType == 1:  # Standard movetype, get player move.
        move = input("Player {name}'s turn. Enter a move: "
                     .format(name=playerTurn))
        while not legitimate(move, playerTurn):
            print('Move was not legitimate.')
            move = input("Player {name}'s turn. Enter a move: "
                         .format(name=playerTurn))
        print()
        return move
    else:  # moveType == 2
        move = input("Player {name}, choose a square: "
                     .format(name=playerTurn))
        while not legitimate(move, playerTurn):
            move = input("Player {name}, choose a square: "
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


def nextTurn(curTurn):
    if curTurn == 1:
        return 2
    else:
        return 1


def captureAndSow(coord, opponentStones):
    location = ORDER.index(coord)
    for i in ORDER[location:] + ORDER[:location]:
        if game.getValue(playerTurn, i) == 0:  # Looking for empty hole
            emptyHole = i
            break
    else:  # No empty hole
        highestValue = max(game.values(playerTurn))

        if Counter(game.values(playerTurn))[highestValue] > 1:  # Choose one
            choices = []
            for i in ORDER:
                if game.getValue(playerTurn, i) == highestValue:
                    choices.append(i)

            print('Possible choices:')
            for i in choices:
                print(i)

            makeMove(move=getMove(2), hand=opponentStones)
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
            captureAndSow(move, opponentStones)


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

    move = getMove(1)
    makeMove(move)

    turnNumber += 1
    playerTurn = nextTurn(playerTurn)

print('Player {playerName} wins!'
      .format(playerName=game.done()))
