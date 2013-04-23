'''
https://www.hackerrank.com/challenges/saveprincess
'''

PRINCESS = 'p'
YOU = 'm'
EMPTY = '-'

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

def _distance(px, py):
	from math import sqrt
	return sqrt(
		(px[1] - px[0]) ** 2
		+
		(py[1] - py[0]) ** 2
	)

def displayPathtoPrincess(n, grid):
	grid = _parse_grid_input(grid)



	pass


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

		res = 2.0

		final = _distance(px, py)

		self.assertEqual(res, final,
			"Sample Input #00. Got %s expected %s." % (final, res))

if __name__ == '__main__':
	unittest.main()