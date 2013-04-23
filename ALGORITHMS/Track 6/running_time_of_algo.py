#!/bin/python
'''
https://www.hackerrank.com/challenges/runningtime

Input Format
The first line contains N, the number of elements to be sorted. The next line 
contains N integers a[1],a[2]...,a[N].

Output Format
Output the number of shifts it takes.

Constraints
1<=s<=1001
-10000 <= x <= 10000 , x \in ar

Sample Input
5
2 1 3 1 2

Sample Output
4

Explanation
The first '1' is shifted once. The '3' stays where it is. The next '1' gets 
shifted twice. The final '2' gets shifted once. The total number of shifts is 
4. 

Task
For this problem, you can copy over your code from InsertionSort and modify it 
to keep track of the number of shifts instead of printing the array.
'''

def insertionSort(ar):
	is_sorted = False
	num = 0
	
	for i,c in enumerate(ar):
		val = ar[i]
		hole = i
		
		# if the val at hole is less than the val before hole,
		# then shift up
		while hole > 0 and val < ar[hole - 1]:
			ar[hole] = ar[hole - 1]
			hole -= 1
			num += 1

		ar[hole] = val

	return num

if False:
	m = input()
	ar = [int(i) for i in raw_input().strip().split()]
	print insertionSort(ar)

import unittest

class SampleCases(unittest.TestCase):

	def testSample00(self):
		ar = [int(x) for x in "2 1 3 1 2".split(" ")]
		res = 4

		final = insertionSort(ar)

		self.assertEqual(res, final,
			"Sample Input #00. Got %s expected %s." % (final, res))


if __name__ == '__main__':
	unittest.main()