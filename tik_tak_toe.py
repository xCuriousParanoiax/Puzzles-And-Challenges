import sys


grid = [
			["-", "-", "-"],
			["-", "-", "-"],
			["-", "-", "-"]
	]

cords_map = {
			"tl": (0,0),
			"tm": (0,1),
			"tr": (0,2),
			"ml": (1,0),
			"mm": (1,1),
			"mr": (1,2),
			"bl": (2,0),
			"bm": (2,1),
			"br": (2,2)
	}

class Game:
	def __init__(self, array):
		self.array = array
		self.playerOne = "X"
		self.playerTwo = "O"
		self.otherPlayer = self.playerTwo
		self.couldComplete = {self.playerOne: self.updated_grid(self.array), self.playerTwo: self.updated_grid(self.array)}

	def updated_grid(self, array):
		'''Returns all possible lines that a player could complete as a list of lists.'''
		rows = array
		columns = [[i[0] for i in array], [i[1] for i in array], [i[2] for i in array]]
		diagonalLeft = [array[0][0], array[1][1], array[2][2]]		# \
		diagonalRight = [array[0][2], array[1][1], array[2][0]]		# /
		diagonalLines = [diagonalLeft, diagonalRight]
		possibleWins = [r for r in rows] + [c for c in columns] + [l for l in diagonalLines]
		return possibleWins

	def print_grid(self, array):
		print()
		for lst in array:
			print("  ".join(lst))
		print()

	def check_if_slot_is_empty(self, slot):
		if slot == "-":
			return True
		return

	def get_coordinates(self, player):
		while True:
			cords = input(f"{player}'s move, select slot: ")
			if cords:
				try:
					return cords_map[cords]
				except KeyError:
					print("Invalid option! Try again")

	def check_if_draw(self):
		'''Ends game with a draw if it's no longer possible for any of the players to complete any of the lines.'''
		possibleWinners = [self.couldComplete[player] for player in self.couldComplete if len(self.couldComplete[player])]
		if not possibleWinners:
			self.print_grid(self.array)
			print("It's a draw!")
			sys.exit()

	def update_completion_possibilities(self, row, column, currentPlayer, otherPlayer):
		'''Calculates what lines a player could win based on whether or not that line includes the other player's name.'''
		self.couldComplete[otherPlayer] = [lst for lst in self.updated_grid(self.array) if not currentPlayer in lst]

	def check_for_winner(self, setOfLists):
		'''Checks for possible winner.'''
		for lst in setOfLists:
			if len(set(lst)) == 1 and not "-" in lst:
				winner = lst[0]
				self.print_grid(self.array)
				print(f"{winner} wins!!!".upper())
				sys.exit()

	def move(self, array, player):
		self.print_grid(array)
		while True:
			lat, _long = self.get_coordinates(player)
			emptySlot = self.check_if_slot_is_empty(array[lat][_long])
			if emptySlot:
				array[lat][_long] = player
				self.update_completion_possibilities(lat, _long, player, self.otherPlayer)
				self.check_if_draw()
				self.check_for_winner(self.updated_grid(array))
				self.otherPlayer = player
				break
			else:
				print("Slot is full! Try again")

	def start(self):
		while True:
			self.move(self.array, self.playerOne)
			self.move(self.array, self.playerTwo)

if __name__ == "__main__":
	Game(grid).start()
