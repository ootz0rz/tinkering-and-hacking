def partition(ar):

	return ""

import unittest

class SampleCases(unittest.TestCase):

	def testSample00(self):
		ar = [int(x) for x in "4 5 3 7 2".split(" ")]
		res = [int(x) for x in "3 2 4 5 7".split(" ")]

		final = insertionSort(ar)

		self.assertEqual(res, final,
			"Sample Input #00. Got %s expected %s." % (final, res))

if __name__ == '__main__':
	unittest.main()