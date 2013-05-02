def add(a=[], b=0):
	'''
	Given an array, a, representation of an integer, add the unsigned integer b
	to a, and return the new a.

	ie: 
	a = [1,2,3,4] => a = 1234

	Ex: 
	a = [1,2,3,4]
	b = 3

	a + b = [1,2,3,7]
	'''
	idx = 1
	cur = b
	carry = 0
	done = False
	while b/10**idx > 0 or carry > 0 or cur > 0 or (b // 10 ** (idx - 1) % 10) > 0:
		# floor ( num / base ^ [place-1] ) % base
		cur = b // 10 ** (idx - 1) % 10
		try:
			res = a[-idx] + cur + carry
		except IndexError:
			a.insert(0, 0)
			res = cur + carry

		a[-idx] = (res % 10)

		carry = res / 10

		idx += 1

	if a[0] == 0 and len(a) > 1:
		a.remove(0)

	return a

if __name__ == '__main__':
	print add([1,2,3], 5) == [1,2,8]
	print add([1,2,5], 5) == [1,3,0]
	print add([0], 5) == [5]
	print add([9], 5) == [1,4]
	print add([9,9,9], 2) == [1,0,0,1]
	print add([9,9,9], 129) == [1,1,2,8]
	print add([0], 0) == [0]