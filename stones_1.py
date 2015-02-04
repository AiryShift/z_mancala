REVERSEMAP = {
    'a': 0,
    'b': 1,
    0: 7,
    1: 6,
    2: 5,
    3: 4,
    4: 3,
    5: 2,
    6: 1,
    7: 0,
}
player1 = [[2 for i in range(8)] for i in range(2)]
player2 = [[2 for i in range(8)] for i in range(2)]


def legit(aMove, curBoard):
    # Determines whether the input is valid
    if len(aMove) != 2:
        return False

    firstChar, secondChar = aMove
    if firstChar not in 'ab':
        return False
    if not secondChar.isnumeric():
        return False
    secondChar = int(secondChar)
    if secondChar not in set(range(1, 9)):
        return False
    if curBoard[REVERSEMAP[firstChar]][secondChar - 1] == 0:
        return False
    return True


def relativePosition(currentPosition, direction):
    # Determines the coordinate of a square forwards or backwards of the given
    answer = []
    if direction == 'forwards':  # Forwards
        if currentPosition[0] == 0:
            if currentPosition[1] == 0:
                answer.append(1)
                answer.append(0)
            else:
                answer.append(0)
                answer.append(currentPosition[1] - 1)
        else:
            if currentPosition[1] == 7:
                answer.append(0)
                answer.append(7)
            else:
                answer.append(1)
                answer.append(currentPosition[1] + 1)
    else:  # Backwards
        if currentPosition[0] == 0:
            if currentPosition[1] == 7:
                answer.append(1)
                answer.append(7)
            else:
                answer.append(0)
                answer.append(currentPosition[1] + 1)
        else:
            if currentPosition[1] == 0:
                answer.append(0)
                answer.append(0)
            else:
                answer.append(1)
                answer.append(currentPosition[1] - 1)
    return answer


def processMove(board, move):
    # Moves the pieces for a player
    startX, startY = move
    hand = board[startX][startY]
    board[startX][startY] = 0
    lookingAt = relativePosition(move, 'forwards')

    while hand > 0:
        board[lookingAt[0]][lookingAt[1]] += 1
        hand -= 1
        lookingAt = relativePosition(lookingAt, 'forwards')

    lookingAt = relativePosition(lookingAt, 'backwards')
    if board[lookingAt[0]][lookingAt[1]] != 1:
        board, lookingAt = processMove(board, lookingAt)

    return board, lookingAt


def getMove(aPlayer):
    # Gets input from the user for a move
    move = input('Move: ')
    while not legit(move, aPlayer):
        print('Illegal move.')
        move = input('Move: ')
    print()

    # Parses the move
    move = list(move)
    move[0] = REVERSEMAP[move[0]]
    move[1] = int(move[1]) - 1
    return move


def makeMove(movingPlayer, opponent):
    # Handles moking stones and stone capture

    # Mokes the pieces for the moving Player
    movingPlayer, lastSpot = processMove(movingPlayer, getMove(movingPlayer))
    if lastSpot[0] == 0:  # If the last stone is dropped in the inner row
        # Remove the opponent's adjacent stones
        opponentsColumn = REVERSEMAP[lastSpot[1]]
        opponent[0][opponentsColumn] = 0
        opponent[1][opponentsColumn] = 0

    return movingPlayer, opponent


def printBoard(printingFor):
    # Outputs the board in a formatted form
    top, bottom = player1, player2
    if printingFor == 1:
        top, bottom = bottom, top

    print("Player {playerNum}'s turn.".format(playerNum=printingFor))
    for i in reversed(top):
        print(' '.join([str(a) for a in reversed(i)]))
    print('-' * 15)
    for i in bottom:
        print(' '.join([str(a) for a in i]))


def notDone(aPlayer):
    # Determines whether any player's win condition has been met.
    for i in aPlayer:
        for j in i:
            if j != 0:
                return True
    return False


currentMove = 1
printBoard(currentMove)

while notDone(player1) and notDone(player2):
    if currentMove == 1:
        player1, player2 = makeMove(player1, player2)
        currentMove = 2
    else:
        player2, player1 = makeMove(player2, player1)
        currentMove = 1

    printBoard(currentMove)

if notDone(player1):
    print('Player 1 wins!')
else:
    print('Player 2 wins!')
