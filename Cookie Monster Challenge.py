import itertools
import collections


lst = ["FOOF", "OCOO", "OOOH", "FOOO"]

expected_answer = 11


# Challenge:
	# Have the function SearchingChallenge(strArr) read the array of strings stored in strArr which will be a 4x4 matrix of the characters 'C', 'H', 'F', 'O'
	# Where C represents Charlie the dog, H represents its home, F represents dog food, and O represents and empty space in the grid.
	# Your goal is to figure out the least amount of moves required to get Charlie to grab each piece of food in the grid by moving up, down, left, or right, and then make it home right after.
	# Charlie cannot move onto the home before all pieces of food have been collected.
	# For the input above, the least amount of steps where the dog can reach each piece of food, and then return home is 11 steps, so your program should return the number 11.
	# The grid will always contain between 1 and 8 pieces of food.


# Examples:

	# Input: ["OOOO", "OOFF", "OCHO", "OFOO"]
	# Output: 7

	# Input: ["FOOO", "OCOH", "OFOF", "OFOO"]
	# Output: 10


def get_coordinates(_list):
	'''create a dict with default values of type: list
	use each letter except for the letter "O" as a key in the dict
	append the letter's coords to its (default) empty list value'''
	coords = collections.defaultdict(list)
	for string_index, string in enumerate(_list, start=1):
		for ltr_index, ltr in enumerate(string, start=1):
			if ltr != "O":
				coords[ltr].append((string_index, ltr_index))
	return coords


def SearchingChallenge(_list, expectedAnswer=None):
	'''get the starting coords of the dog
	get the coords of the home
	get the coords for the cookies
	calculate each possible order in which the dog could eat the cookies in using permutations
	calculate how many steps the dog would need to take in order to eat all of the cookies in a given order
	do that by calculating the distance between the dog and the first cookie in the given order of cookies and then the distance from that cookie to the next one
	add to that the number of steps the dog would need to take in order to return home after eating the cookies
	if an expected answer was given, and the number of steps taken matches the expected answer, print "Solved!" and return None to break out of the loop
	if we don't know the expected answer, then append the number of steps that were taken to a list
	reset the number of steps taken to 0 and reset the position of the dog to its original position
	do that for each possible order until you match the expected answer if one was given
	if not, print the minimum value from the list in which you appended the number of steps taken for each order'''
	walked = 0
	possible_routs = []
	coordinates = get_coordinates(_list)
	dog_started_at, dog_dest, stops = coordinates["C"][0], coordinates["H"][0], coordinates["F"]
	dog_at = dog_started_at
	combinations = [i for i in itertools.permutations(stops, len(stops))]
	for combination in combinations:
		for cord in combination:
			walked += sum((abs(dog_at[0]-cord[0]), abs(dog_at[1]-cord[1])))
			dog_at = cord
		walked += sum((abs(dog_at[0]-dog_dest[0]), abs(dog_at[1]-dog_dest[1])))
		if expectedAnswer:
			if walked == expectedAnswer:
				print("Solved!")
				return
		else:
			possible_routs.append(walked)
		walked = 0
		dog_at = dog_started_at
	print(min(possible_routs))

SearchingChallenge(lst)
SearchingChallenge(lst, expected_answer)
