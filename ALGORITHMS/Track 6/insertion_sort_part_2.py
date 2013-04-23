#!/bin/python
'''
In Insertion Sort Part 1, you sorted one element into an array. Using the same 
approach repeatedly, can you sort an entire unsorted array?

Guideline: You already can place an element into a sorted array. How you can 
you use that code to build up a sorted array, one element at a time? Note that 
the first element is already "sorted" since there's nothing to its left that is 
smaller than it.

In this challenge, don't print every time you move an element. Instead, print 
the array every time an element is "inserted" into the array in (what is 
currently) its correct place. Since the first element is already "sorted", 
begin printing from the second element and on.

Input Format
There will be two lines of input:

    s - the size of the array
    ar - the list of numbers that makes up the array

Output Format
On each line, output the entire array every time an item is inserted into its 
place.

Constraints
1<=s<=1000
-10000<=x<= 10000 , x ? ar

Sample Input

6
1 4 3 5 6 2

Sample Output

1 4 3 5 6 2 
1 3 4 5 6 2 
1 3 4 5 6 2 
1 3 4 5 6 2 
1 2 3 4 5 6 

Explanation
Insertion Sort checks the '4' first and doesn't need to move it, so it just 
prints out the array. Next, the 3 is inserted next to the 4 and the array is 
printed out. This continues one element at a time until the entire array is 
sorted.

Task
The method insertionSort takes in one parameter: ar, an unsorted array. Use an Insertion Sort Algorithm to sort the entire array. 
'''

def printarr(ar):
	print " ".join([str(x) for x in ar])

def insertionSort(ar):
	is_sorted = False
	
	for i,c in enumerate(ar):
		val = ar[i]
		hole = i
		
		# if the val at hole is less than the val before hole,
		# then shift up
		while hole > 0 and val < ar[hole - 1]:
			ar[hole] = ar[hole - 1]
			hole -= 1

		ar[hole] = val

		if i > 0:
			printarr(ar)

	return ar

import unittest

class SampleCases(unittest.TestCase):

	def testSample00(self):
		ar = [int(x) for x in "1 4 3 5 6 2".split(" ")]
		res = [int(x) for x in "1 2 3 4 5 6".split(" ")]

		final = insertionSort(ar)

		self.assertEqual(res, final,
			"Sample Input #00. Got %s expected %s." % (final, res))

	def test01(self):
		ar = [int(x) for x in "2 3 4 5 1".split(" ")]
		res = [int(x) for x in "1 2 3 4 5".split(" ")]

		final = insertionSort(ar)

		self.assertEqual(res, final,
			"Test Input #01. Got %s expected %s." % (final, res))

	def test02(self):
		ar = [int(x) for x in "2 3 4 5 2".split(" ")]
		res = [int(x) for x in "2 2 3 4 5".split(" ")]

		final = insertionSort(ar)

		self.assertEqual(res, final,
			"Test Input #02. Got %s expected %s." % (final, res))

	def test03(self):
		ar = [int(x) for x in "1 2 3 4".split(" ")]
		res = [int(x) for x in "1 2 3 4".split(" ")]

		final = insertionSort(ar)

		self.assertEqual(res, final,
			"Test Input #03. Got %s expected %s." % (final, res))

	def test04(self):
		ar = [int(x) for x in "5 1 2 3 4".split(" ")]
		res = [int(x) for x in "1 2 3 4 5".split(" ")]

		final = insertionSort(ar)

		self.assertEqual(res, final,
			"Test Input #04. Got %s expected %s." % (final, res))

	def testbase01(self):
		ar = [int(x) for x in "1 2 4 5 3".split(" ")]
		res = [int(x) for x in "1 2 3 4 5".split(" ")]

		final = insertionSort(ar)

		self.assertEqual(res, final,
			"Base Input #01. Got %s expected %s." % (final, res))


if __name__ == '__main__':
	unittest.main()