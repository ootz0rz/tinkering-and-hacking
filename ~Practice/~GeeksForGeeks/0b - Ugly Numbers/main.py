'''
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence:

1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ...

shows the first 11 ugly numbers. By convention, 1 is included.

Write a program to find and print the 150'th ugly number.



i.e. It's ugly if its only factors are 2, 3 or 5
'''

def isUgly(n):
	if n % 2 == 0:
		return isUgly(n / 2)

	elif n % 3 == 0:
		return isUgly(n / 3)

	elif n % 5 == 0:
		return isUgly(n / 5)

	else:
		return n == 1

def UN(n=150):
	'''
	Print the n-th Ugly Number
	'''

	count = 0
	i = 0
	while count < n:
		i += 1

		if isUgly(i):
			count += 1

	return i

def UNdp(n=150):
	'''
	Print the 150th Ugly Number using Dynamic Programming.
	'''
	pass