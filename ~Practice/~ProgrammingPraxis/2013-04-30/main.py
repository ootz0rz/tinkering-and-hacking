'''
First Unrepeated Character In A String
April 30, 2013

We have today another exercise from our never-ending supply of interview 
questions:

    Given a string, find the first character that appears only once in the 
    string. For instance, given the string "aabbcddd", the first character 
    that appears only once is the "c" found at the 4th character in the string, 
    counting from 0. Be sure that your program properly handles the case that 
    all characters appear more than once.

Your task is to write a program that finds the first unrepeated character in a 
string, and its index in the string. When you are finished, you are welcome to 
read or run a suggested solution, or to post your own solution or discuss the 
exercise in the comments below.
'''

def first(s):
	'''
	Return a tuple (index, character) of the first unique character in the 
	string s. 

	Note:
		Tried to make it as fast as possible in run time...
		O(2n) => O(n)
		But uses the same in additional memory.
	'''
	visited = {}
	unique_idx = {}

	for idx, c in enumerate(s):
		if not c in visited:
			unique_idx[c] = idx
			visited[c] = 1

		else:
			if c in unique_idx:
				del unique_idx[c]

	if not unique_idx:
		return None
	else:
		# make sure we return the first one in order...since no order gaurantee
		# from hashsets
		for idx, c in enumerate(s):
			if c in unique_idx:
				return (idx, c)

print first("c") == (0, 'c')
print first("caa") == (0, 'c')
print first("aac") == (2, 'c')
print first("aabbcddd") == (4, 'c')
print first("aabbcddde") == (4, 'c')
print first("aabbddd") == None