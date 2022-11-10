from typing import List, Optional, Dict

# stupid...but works
import sys, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from TestHarness import *

'''
function fn(arr):
    left = 0
    for right in [0, arr.length - 1]:
        Do some logic to "add" element at arr[right] to window

        while left < right AND condition from problem not met:
            Do some logic to "remove" element at arr[left] from window
            left++

        Do some logic to update the answer
'''

def longest_subarray_sum_less_than_k(k, nums):
    '''
    Given an array of positive integers nums and an integer k, find the length of the longest 
    subarray whose sum is less than or equal to k.
    '''
    left = 0
    val = 0
    max_len = 0

    for right in range(len(nums)):
        val += nums[right]

        while val > k:
            val = val - nums[left]
            left = left + 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len 
    '''
    O(n) since we go through each value in nums at most once, while keeping track of the sum of the sub-array
    to compare so we don't have to iterate over it again. All we do is remove elements from the sub-array,
    which could incur at most n more accesses but that's amortized over the run of the entire 
    outer loop @ O(2n)
    '''

'''
check_solution_simple(longest_subarray_sum_less_than_k, args=[8, [3,1,2,7,4,2,1,1,5]], expected=len([4,2,1,1]))
'''


def longest_binary_substr(s):
    '''
    You are given a binary substring s (a string containing only "0" and "1"). An operation involves 
    flipping a "0" into a "1". What is the length of the longest substring containing only "1" after 
    performing at most one operation?

    For example, given s = "1101100111", the answer is 5. If you perform the operation at index 2, 
    the string becomes 1111100111.
    '''

    '''
    Idea is to find the longest str with only a single '0' in it
    '''

    '''
    function fn(arr):
        left = 0
        for right in [0, arr.length - 1]:
            Do some logic to "add" element at arr[right] to window

            while left < right AND condition from problem not met:
                Do some logic to "remove" element at arr[left] from window
                left++

            Do some logic to update the answer
    '''
    left = 0
    num_z = 0
    max_len = 0

    for right in range(len(s)):
        if s[right] == '0'
            num_z = num_z + 1
        
        # remove from left until we have num_z <= 1
        while num_z > 1:
            if s[left] == '0'
                num_z = num_z - 1
            left = left + 1
        
        # check len of current window vs previous max
        max_len = max(max_len, right - left + 1)
    
    return max_len
        
def subarray_prod_less_than_k(nums, k):
    '''
    713. Subarray Product Less Than K.

    Given an array of positive integers nums and an integer k, return the number of contiguous 
    subarrays where the product of all the elements in the subarray is strictly less than k.

    For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. The subarrays 
    with products less than k are:

    [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
    '''

    '''
    Note, once we've found the largest valid window before we have to start moving up the left side again,
    we know that we've now found len(win) number of subsets that can be added to the total

    and len(win) = right - left + 1
    '''
    
    left = 0
    curr_val = 0
    total_num = 0

    while right < range(len(nums)):
        curr_val = curr_val * nums[right]

        while left < right and curr_val > k:
            curr_val = curr_val // nums[left] # // to keep as int
            left = left + 1
        
        total_num = total_num + (right - left + 1)
    
    return total_num

### --------------------------------------------------------------------------
### --------------------------------------------------------------------------
### fixed subarray size
### --------------------------------------------------------------------------
### --------------------------------------------------------------------------

'''
// first approach
function fn(arr, k):
    curr = some data type to track the window

    // build the first window
    for i in [0, k - 1]:
        Do something with curr or other variables to build first window

    ans = answer variable, might be equal to curr here depending on the problem
    for i in [k, arr.length - 1]:
        Add arr[i] to window
        Remove arr[i - k] from window
        Update ans

    return ans

// second approach
function fn(arr, k):
    curr = some data type to track the window
    ans = answer variable
    for i in range(len(arr)):
        if i >= k:
            Update ans
            Remove arr[i - k] from window
        Add arr[i] to window

    Update ans    
    return ans //   Alternatively, you could do something like return max(ans, curr) if the problem is asking for a 
                    maximum value and curr is tracking that.
'''

def largest_sum_subarray_len_k(nums, k):
    '''
    Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.
    '''
    curr = 0
    for i in range(k):
        curr += nums[i]
    
    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)
    
    return ans

### --------------------------------------------------------------------------
### --------------------------------------------------------------------------
### --------------------------------------------------------------------------
### --------------------------------------------------------------------------
### --------------------------------------------------------------------------

'''
function fn(arr):
    curr = some data type to track the window

    // build the first window
    for i in [0, k - 1]:
        Do something with curr or other variables to build first window

    ans = answer variable, might be equal to curr here depending on the problem
    for i in [k, arr.length - 1]:
        Add arr[i] to window
        Remove arr[i - k] from window
        Update ans

    return ans
'''

# https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4594/
def findMaxAverage(nums: List[int], k: int) -> float:
    curr_avg = 0
    max_avg = 0

    # build initial subarray
    for i in range(k):
        curr_avg = curr_avg + (nums[i] / k)

    max_avg = curr_avg
    for i in range(k, len(nums)):
        curr_avg = curr_avg + (nums[i] / k)
        curr_avg = curr_avg - (nums[i - k] / k)

        max_avg = max(max_avg, curr_avg)
    
    return max_avg

'''
function fn(arr):
    left = 0
    for right in [0, arr.length - 1]:
        Do some logic to "add" element at arr[right] to window

        while left < right AND condition from problem not met:
            Do some logic to "remove" element at arr[left] from window
            left++

        Do some logic to update the answer
'''
# https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4595/
def longestOnes(nums: List[int], k: int) -> int:
    left = 0
    cur_z = 0
    max_len = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            cur_z = cur_z + 1

        while cur_z > k:
            if nums[left] == 0:
                cur_z = cur_z - 1
            left = left + 1

        max_len = max(max_len, right - left + 1)

    return max_len