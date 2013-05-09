'''
https://www.hackerrank.com/challenges/quicksort2


'''

def quickSort(ar):
	if len(ar) < 1:
		return []

	left = []
	right = []
	pivot = ar[0]

	for i,c in enumerate(ar[1:]):
		if c > pivot:
			right.append(c)
		else:
			left.append(c)

	final = quickSort(left) + [pivot] + quickSort(right)

	if len(final) > 1:
		print " ".join([str(x) for x in final])
		
	return final

import unittest

class SampleCases(unittest.TestCase):

	def testSample00(self):
		ar = [int(x) for x in "5 8 1 3 7 9 2".split(" ")]
		res = [int(x) for x in "1 2 3 5 7 8 9".split(" ")]

		final = quickSort(ar)

		self.assertEqual(res, final,
			"Sample Input #00. Got %s expected %s." % (final, res))

if __name__ == '__main__':
	unittest.main()