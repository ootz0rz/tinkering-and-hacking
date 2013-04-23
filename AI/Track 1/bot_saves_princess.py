'''
https://www.hackerrank.com/challenges/saveprincess
'''
from math import sqrt

# for input grid
PRINCESS = 'p'
YOU = 'm'
EMPTY = '-'

# valid moves/outputs
UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"

def _parse_grid_input(grid):
	'''
	Return a 3-tuple:
		First the grid parsed, as an array of arrays

		Then the position of your character as a tuple (x, y)

		Then the position of the princess as a tuple (x, y)
	'''

	res = []
	you_pos = []
	prin_pos = []
	for i,line in enumerate(grid.split("\n")):

		res_line = []
		for j,char in enumerate(line):
			if char == EMPTY:
				res_line.append(EMPTY)

			elif char == YOU:
				res_line.append(YOU)
				you_pos = (j,i)

			elif char == PRINCESS:
				res_line.append(PRINCESS)
				prin_pos = (j,i)

		res.append(res_line)

	return (res, you_pos, prin_pos)

def _distance((x1, y1), (x2, y2)):
	'''
	Euclidean distance between px, py, each given as tuple (x, y)
	'''
	
	return sqrt(
		(x2 - x1) ** 2
		+
		(y2 - y1) ** 2
	)

def _get_new_pos(grid, direction, cur):
	'''
	Given the grid, direction to move (UP DOWN LEFT RIGHT) and your current
	position as a tuple (x, y), compute new position taking grid bounds into 
	consideration.
	'''

	if direction == RIGHT:
		if (cur[0] + 1) < len(grid):
			cur = [cur[0] + 1, cur[1]]

	elif direction == LEFT:
		if (cur[0] - 1) >= 0:
			cur = [cur[0] - 1, cur[1]]

	elif direction == UP:
		if (cur[1] - 1) >= 0:
			cur = [cur[0], cur[1] - 1]

	elif direction == DOWN:
		if (cur[1] + 1) < len(grid[cur[0]]):
			cur = [cur[0], cur[1] + 1]

	return cur

def displayPathtoPrincess(n, grid):
	grid, me, target = _parse_grid_input(grid)

	reached_target = False

	cur_pos = [me[0], me[1]]

	move_list = (UP, DOWN, LEFT, RIGHT)

	moves_used = []

	while not (
			# reached target?
			cur_pos[0] == target[0] and cur_pos[1] == target[1]
		):

		# get possible moves
		newpos = (
			_get_new_pos(grid, move_list[0], cur_pos), 
			_get_new_pos(grid, move_list[1], cur_pos), 
			_get_new_pos(grid, move_list[2], cur_pos), 
			_get_new_pos(grid, move_list[3], cur_pos))

		# get new distances to target
		tup = (
			_distance(target, newpos[0]), 
			_distance(target, newpos[1]), 
			_distance(target, newpos[2]),
			_distance(target, newpos[3]))

		# find min
		min_index = min(xrange(len(tup)), key=tup.__getitem__)

		# update position+move
		cur_pos = newpos[min_index]
		moves_used.append(move_list[min_index])

	return "\n".join(moves_used)

import unittest

class GridParse(unittest.TestCase):

	def testSample00(self):
		grid = "---\n-%s-\n%s--" % (YOU, PRINCESS)
		resgrid = [
			[EMPTY, EMPTY, EMPTY],
			[EMPTY, YOU, EMPTY],
			[PRINCESS, EMPTY, EMPTY]
		]
		resyoupos = (1, 1)
		resprinpos = (0, 2)
		res = (resgrid, resyoupos, resprinpos)

		final = _parse_grid_input(grid)

		self.assertEqual(res, final,
			"Sample Input #00. Got %s expected %s." % (final, res))

class DistanceCalc(unittest.TestCase):

	def testSample00(self):
		px = (0,0)
		py = (0,2)

		res = sqrt(2**2)

		final = _distance(px, py)

		self.assertEqual(res, final,
			"Sample Input #00. Got %s expected %s." % (final, res))

	def testSample01(self):
		px = (0,2)
		py = (1,1)

		res = sqrt((2 - 1)**2 + (0 - 1)**2)

		final = _distance(px, py)

		self.assertEqual(res, final,
			"Sample Input #01. Got %s expected %s." % (final, res))

class PathDisplay(unittest.TestCase):

	def testSample00(self):
		grid = "---\n-%s-\n%s--" % (YOU, PRINCESS)
		res = "DOWN\nLEFT"

		final = displayPathtoPrincess(3, grid)

		self.assertEqual(res, final,
			"Sample Input #00. Got %s expected %s." % (final, res))

if __name__ == '__main__':
	unittest.main()