'''
https://www.hackerrank.com/challenges/quicksort1


'''


def partition(ar):
	left = []
	right = []
	pivot = ar[0]

	for i,c in enumerate(ar[1:]):
		if c > pivot:
			right.append(c)
		else:
			left.append(c)

	print " ".join([str(x) for x in left + [pivot] + right])
	return left + [pivot] + right

import unittest

class SampleCases(unittest.TestCase):

	def testSample00(self):
		ar = [int(x) for x in "4 5 3 7 2".split(" ")]
		res = [int(x) for x in "3 2 4 5 7".split(" ")]

		final = partition(ar)

		self.assertEqual(res, final,
			"Sample Input #00. Got %s expected %s." % (final, res))

if __name__ == '__main__':
	unittest.main()