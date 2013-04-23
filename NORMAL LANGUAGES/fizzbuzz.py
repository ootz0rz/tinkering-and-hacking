for x in range(16):
	if x % 3 == 0:
		print "Fizz",

	if x % 5 == 0:
		print "Buzz",

	if x % 3 != 0 and x % 5 != 0:
		print x,

	print