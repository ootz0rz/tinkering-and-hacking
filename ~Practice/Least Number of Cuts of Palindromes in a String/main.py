def MinCuts(S):
	'''
	Return the minimum cut configurations of S such that each cut is a 
	palindrome.
	'''

	m = SubPalindromes(S)

	return _minCuts(list(S), m, {}, 1, 0)

def _minCuts(L, subs, mem = {}, n = 1, i1 = 0):
	'''
	n = number of consecutive cuts to remove
	'''

	# init mem
	minNum = len(L)

	if not minNum in mem:
		mem[minNum] = []
		mem[minNum].append(L)

	i = 0
	for idx, el in enumerate(L):
		j = len(el)

		if (idx+n) < len(L):
			# construct an element by removing the next n cuts
			s = ""
			for m in xrange(n):
				s = s + L[idx + m]
			j = len(s)

			# check if it's valid
			if subs[i][j]:
				# create and modify a copy, L2, to match our changes
				L2 = L[::]
				L2[idx] = s

				for m in xrange(1, n):
					del L2[idx + m]

				# recurse for the rest of it
				L2 = L2[:idx + 1] + _minCuts(L2[idx + 1:], subs, mem, n, i1 + len(s))

				newNum = len(L2)

				# add to memo
				if not newNum in mem:
					mem[newNum] = []

				mem[newNum].append(L2)

				if newNum < minNum:
					minNum = newNum
		else:
			# no point in continuing if we can't remove any more cuts
			break

		i += j

	min_1 = mem[minNum]
	min_2 = _minCuts(L, subs, mem, n + 1, i1 = 0)

	len_min1 = len(min_1)
	len_min2 = len(min_2)
	
	return min_1 if len_min1 < len_min2 else min_2

def _isValid(L, subs):
	'''
	Return true iff every element in L is a palindrome as defined in subs.

	O(n)
	'''

	i = 0
	for idx,el in enumerate(L):
		j = len(el)

		if not subs[i][j]:
			return False

		i += j
	return True

def ISP(x):
	'''
	True iff x is a palindrome.

	O(n) if we take string comparison as O(1), else O(n^2)
	'''
	return x == x[::-1]

def ISPSub(i, j, subs):
	return subs[i:j]

def SubPalindromes(S):
	'''
	Return a table m[i][j] s.t. m[i][j] = ISP(S[i:j])

	O(n^2) if we consider ISP(s) to run in O(1). Else O(n^2 * O(ISP))
	'''
	m = {}

	for i,c1 in enumerate(S): # n
		m[i] = {}

		for j,c2 in enumerate(S): # n

			s = S[i:j+1]
			m[i][j] = ISP(s)

			print 'ISP(%s) -> %s' % (s, m[i][j])

	return m