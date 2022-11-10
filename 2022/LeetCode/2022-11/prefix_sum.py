from typing import List, Optional, Dict

# stupid...but works
import sys, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from TestHarness import *

'''
Prefix sums allow us to find the sum of any subarray in O(1)O(1). 
If we want the sum of the subarray from i to j (inclusive), then the answer is prefix[j] - prefix[i - 1], 
or prefix[j] - prefix[i] + nums[i] if you don't want to deal with the out of bounds case when i = 0.

Building a prefix sum is very simple. Here's some pseudocode:

Given an integer array nums,

prefix = [nums[0]]
for i in [1, len(nums) - 1]:
    prefix.append(nums[i] + prefix[prefix.length - 1])
'''

'''
Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array 
that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, 
or false otherwise.

For example, given nums = [1, 6, 3, 2, 7, 2] and queries = [[0, 3], [2, 5], [2, 4]] and limit = 13, the answer is 
[true, false, true]. For each query, the subarray sums are [12, 14, 12].
'''

def answer_queries(nums, queries, limit):
    
    # first build prefix sum array
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    ans = []
    for i,j in queries:
        sum = prefix[j] - prefix[i] + nums[i]
        ans.append(sum < limit)
    
    return ans 
    '''
    This is O(n+m), it takes O(n) to build the prefix array and then we can answer each query in O(1) time.
    There are m queries, so O(m) to answer them all. 
    '''

# https://leetcode.com/problems/number-of-ways-to-split-array/
def waysToSplitArray(nums: List[int]) -> int:
    '''
    2270. Number of Ways to Split Array

    Given an integer array nums, find the number of ways to split the array into two parts so that the first 
    section has a sum greater than or equal to the sum of the second section. The second section should have at least 
    one number.
    '''
    # first build prefix sum array
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    num_ways = 0
    for i in range(len(prefix) - 1): # note, we do -1 because we want to make sure 'right side' has at least 1 element

        # we could probably also build left_sum on the fly... adding nums[i] to it every iteration instead of
        # having to build the prefix sum above first? Since we're always gradually expanding left_sum as we go along
        # in this case
        left_sum = prefix[i]
        right_sum = prefix[-1] - prefix[i]

        if left_sum >= right_sum:
            num_ways = num_ways + 1

    return num_ways 

# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4658/
def runningSum(self, nums: List[int]) -> List[int]:
    '''
    literally just the prefix sums?
    '''
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    return prefix

# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4657/
def minStartValue(nums: List[int]) -> int:
    # prefix sums
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    '''
    O(n) to build
    ''' 

    # choose a value k starting at 1, make sure k + prefix[i] >= 1 for all i in prefix, find smallest k
    k = 0
    while True:        
        k = k + 1

        i = len(prefix) - 1

        while (k + prefix[i]) >= 1 and i >= 0:
            i = i - 1

        if i < 0: # if we've gone through all values of nums for this value of k, we're good to go
            return k

    return k 

check_solution_simple(minStartValue, args=[[1,2]], expected=1)
check_solution_simple(minStartValue, args=[[-3,2,-3,4,2]], expected=5)
check_solution_simple(minStartValue, args=[[1,-2,-3]], expected=5)