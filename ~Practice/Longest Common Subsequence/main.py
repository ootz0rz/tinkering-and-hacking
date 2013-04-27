'''
See readme.md for what this code is based off of.
'''

def LCS(X, Y, mem={}):
	'''
	Compute the Longest Common Subsequence of sequences X and Y
	'''

	i = len(X)
	j = len(Y)

	# init mem
	if not (i in mem):
		mem[i] = {}

	if not (j in mem[i]):
		mem[i][j] = []
	
	# LCS of any set and an empty set is the empty set
	if i == 0 or j == 0:
		mem[i][j] = []

	# Case 1: endings are same
	elif X[-1] == Y[-1]:
		mem[i][j] = \
			LCS(X[:-1], Y[:-1], mem) + [X[-1]]

	# Case 2: endings are not the same
	elif X[-1] != Y[-1]:
		mX = LCS(X[:-1], Y, mem)
		mY = LCS(X, Y[:-1], mem)

		if len(mX) > len(mY):
			mem[i][j] = mX
		else:
			mem[i][j] = mY

	return mem[i][j]

if __name__ == '__main__':
	X = list("ACBDEGCEDBG")
	Y = list("BEGCFEUBK")

