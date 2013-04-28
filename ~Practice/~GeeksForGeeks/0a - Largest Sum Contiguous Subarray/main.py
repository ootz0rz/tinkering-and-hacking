def LSCS(L):
	'''
	Find the sum of contiguous subarray within a one-dimensional array of 
	numbers which has the largest sum.

	Basically, we loop through and keep track of the current sum. If the sum
	is greater than the last max sum, we update the max sum. If the current
	sum becomes less than 0, then we set current sum to 0 and continue through
	the array.
	'''

	curmax = 0
	summax = 0

	for i in L:
		summax += i

		if summax < 0:
			summax = 0

		if curmax < summax:
			curmax = summax

	return curmax

if __name__ == '__main__':
	l = [-2, -3, 4, -1, -2, 1, 5, -3]

	print LSCS(l) == 7