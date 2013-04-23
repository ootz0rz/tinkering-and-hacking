def parlor(C, plist):
	for i,c1 in enumerate(plist):
		for j,c2 in enumerate(plist):
			if c1 + c2 == C and i != j:
				l = [i+1,j+1]
				l.sort()
				return l

import unittest

class ParlorTricks(unittest.TestCase):

	def testSample00(self):
		C = 4
		L = 5
		plist = [1,4,5,3,2]
		res = " ".join([str(x) for x in [1, 4]])

		final = " ".join([str(x) for x in parlor(C, plist)])

		self.assertEqual(res, final,
			"Sample Input #00. Got %s expected %s." % (final, res))

	def testSample01(self):
		C = 4
		L = 4
		plist = [2,2,4,3]
		res = " ".join([str(x) for x in [1, 2]])

		final = " ".join([str(x) for x in parlor(C, plist)])

		self.assertEqual(res, final,
			"Sample Input #01. Got %s expected %s." % (final, res))

if __name__ == '__main__':
	if True:
		unittest.main()

	else:
		T = int(input())

		for x in range(T):
			C = int(input())
			L = int(input())

			plist = [int(x) for x in raw_input().split(" ")]

			print " ".join([str(x) for x in parlor(C, plist)])