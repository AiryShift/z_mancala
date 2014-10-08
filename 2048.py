from random import randrange
# This was a bad idea.
###
# Fills the empty spot after a turn
def check(table):
	output = []
	for i in range(len(table)):
		for j in range(len(i)):
			if table[i][j] == 0:
				output.append([i, j])
	return output

def choose_spot(available):
	return avaliable[randrange(len(avaliable))]

def choose_val():
	num = randrange(10)
	if num == 0:
		return 4
	return 2

def fill_spot(table):
	spot = choose_spot(check(table))
	val = choose_val()
	table[spot[0]][spot[1]] = val
	return table
###
def move(direction, board):
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
				i[j] = ' '
			i[j] = ' ' * (length - len(i[j])) + i[j]
		print(' '.join(i))
	print('\n')
###
def execute(task):
	global board
	global prevBoard
	if task == 'init':
		board = [[[0] for i in range(4)] for j in range(4)]
		for i in range(2):
			board = fill_spot(board)
	elif task == 'u' or task == 'd' or task == 'l' or task == 'r':
		board = move(task, board)
		board = fill_spot(board)
		print_board(board)
	elif task == 'undo':
		board = prevBoard
		print_board(board)
	elif task == 'help':
		# TODO: HALP
		print('Sorry, no help avaliable')
	else:
		print('Enter a known command.')
board = [[[0] for i in range(4)] for j in range(4)]
while True:
	prevBoard = board
	execute(input('Command: '))
