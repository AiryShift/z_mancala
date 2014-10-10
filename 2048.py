from random import randrange
# This was a bad idea.
###
# Fills the empty spot after a turn
def check(table):
	output = []

	#return list of all empty spots ('0') 
	for i in range(len(table)):
		for j in range(len(i)):
			if table[i][j] == 0:
				output.append([i, j])
	return output

def choose_spot(available):
	#return random empty spot given list of empty spots
	return available[randrange(len(available))]

def choose_val():
	#random value
	num = randrange(10)
	if num == 0:
		return 4
	return 2

def fill_spot(table):
	#fill spot in table with value
	spot = choose_spot(check(table)) #empty spot
	val = choose_val() #random value 2, 4
	table[spot[0]][spot[1]] = val
	return table #return updated table
###
def win_loss(board):
	# Returns True if lost
	# checks if can move in each direction
	if not can_move('u', board):
		if not can_move('d', board):
			if not can_move('l', board):
				if not can_move('r', board):
					return True #LOST
	return False #CONTINUE

def can_move(direction, board):
	available = check(board)
	pass
	return True

def move(direction, board):
	if direction == 'u':
		pass
	elif direction == 'd':
		pass
	elif direction == 'l':
		pass
	elif direction == 'r':
		pass
	return board
###
def print_board(table):
	# Determines the largest number
	maxi = table[0][0]
	for i in table:
		for j in i:
			maxi = max(maxi, j)
	length = len(str(maxi))
	# Adds whitespace while printing
	for i in table:
		i = [str(x) for x in i]
		for j in range(len(i)):
			if i[j] == 0:
				i[j] = '.'
			i[j] = ' ' * (length - len(i[j])) + i[j]
		print(' '.join(i))
	print('\n')
###
def execute(task):
	global board
	global prevBoard
	if task == 'init':
		#create game boards
		#board 4 x 4 squares
		board = [[[0] for i in range(4)] for j in range(4)]
		prevBoard = [[[0] for i in range(4)] for j in range(4)]
		for i in range(2):
			board = fill_spot(board)
		print_board(board)

	elif task == 'u' or task == 'd' or task == 'l' or task == 'r':
		if can_move(task, board):
			board = move(task, board)
			board = fill_spot(board)
			print_board(board)
		else:
			print('Choose another direction.')
		if win_loss(board):
			print('You lose.')
			execute('init')
	elif task == 'undo':
		board = prevBoard
		print_board(board)
	elif task == 'help':
		# TODO: HALP
		print('Sorry, no help available')
	else:
		print('Enter a known command.')

#array of '0's 4 x 4 
board = [[[0] for i in range(4)] for j in range(4)]

while True:
	prevBoard = board
	execute(input('Command: '))
