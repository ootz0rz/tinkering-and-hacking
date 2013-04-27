'''
See readme.md for what this code is based off of.
'''

def LCSPrefix(X, Y, mem={}):
	'''
	Compute Longest Common Suffix X and Y, and return result
	'''

	i = len(X)
	j = len(Y)

	# init mem
	if not (i in mem):
		mem[i] = {}

	if not (j in mem[i]):
		mem[i][j] = ""
	
	# LCS of any string and an empty string is empty string
	if i == 0 or j == 0:
		mem[i][j] = ""

	elif X[-1] == Y[-1]:
		mem[i][j] = LCSPrefix(X[:-1], Y[:-1]) + X[-1]

	elif X[-1] != Y[-1]:
		mem[i][j] = ""

	return mem[i][j]

def _LCS(X, Y, mem={}):
	'''
	Compute and return all Longest Common Substring of X, Y as a list
	'''

	s1 = ""
	s2 = ""
	maxLength = 0

	for x in X:
		s1 = s1 + x
		s2 = ""

		for y in Y:
			s2 = s2 + y

			lcp = LCSPrefix(s1, s2)
			length = len(lcp)

			if not length in mem:
				mem[length] = []

			mem[length].append(lcp)

			if length > maxLength:
				maxLength = length

	return mem[maxLength]

def LCS(X, Y):
	'''
	Compute and return all Longest Common Substring of X, Y as a list
	'''
	return _LCS(X, Y, {})


if __name__ == '__main__':
	X = "ABCD"
	Y = "DABC"

	res = ["ABC"]

	print LCS(X, Y) == res