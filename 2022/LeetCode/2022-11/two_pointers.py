from typing import List, Optional, Dict

# stupid...but works
import sys, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from TestHarness import *

def is_palindrome(s):
    '''
    Return true if a given string is a palindrome, false otherwise.

    A string is a palindrome if it reads the same forwards as backwards. That means, after reversing it, 
    it is still the same string. For example: "abcdcba", or "racecar".
    '''
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
            continue

        if s[i] != s[j]:
            return False
    
    return True
    '''
    O(n) because we only check each char in the string at most once
    '''
'''
check_solution_simple(is_palindrome, args=[""], expected=True)
check_solution_simple(is_palindrome, args=["a"], expected=True)
check_solution_simple(is_palindrome, args=["aa"], expected=True)
check_solution_simple(is_palindrome, args=["aba"], expected=True)
check_solution_simple(is_palindrome, args=["abc"], expected=False)
check_solution_simple(is_palindrome, args=["acaa"], expected=False)
check_solution_simple(is_palindrome, args=["aaca"], expected=False)
check_solution_simple(is_palindrome, args=["daac"], expected=False)
'''

def does_sum_to_target(arr, target):
    '''
    Given a sorted array of unique integers and a target integer, return true if there exists a pair of 
    numbers that sum to target, false otherwise. This problem is similar to Two Sum.

    For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.
    '''
    
    i = 0
    j = len(arr) - 1

    while i < j:
        s = arr[i] + arr[j]
        if s == target:
            return True

        if s < target:
            # we're smaller than target, find a larger number to use
            i += 1
        elif s > target:
            # we're bigger than target, find a smaller number to use
            j -= 1
    
    return False
    '''
    O(n) because numbers are sorted, we're able to take a shortcut here to iteratively almost 'search' 
    for the solution from either end
    '''
'''
check_solution_simple(does_sum_to_target, args=[[1,2], 3], expected=True)
check_solution_simple(does_sum_to_target, args=[[1,2], 4], expected=False)
check_solution_simple(does_sum_to_target, args=[[1,2,4,8], 6], expected=True)
check_solution_simple(does_sum_to_target, args=[[1,2,4,8], 9], expected=True)
check_solution_simple(does_sum_to_target, args=[[1,2,4,8], 3], expected=True)
check_solution_simple(does_sum_to_target, args=[[1,2,4,8], 4], expected=False)
check_solution_simple(does_sum_to_target, args=[[1,2,3,4,8], 5], expected=True)
check_solution_simple(does_sum_to_target, args=[[1,2,3,4,8], 16], expected=False)
check_solution_simple(does_sum_to_target, args=[[1,2,3,4,8], 0], expected=False)
check_solution_simple(does_sum_to_target, args=[[1,2,4,6,8,9,14,15], 13], expected=True)
'''

def merge_sorted_arrays(arr1, arr2):
    '''
    Given two sorted integer arrays, return an array that combines both of them and is also sorted.
    '''
    o = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            # consume arr1
            o.append(arr1[i])
            i = i + 1
        elif arr1[i] >= arr2[j]:
            # consume arr2
            o.append(arr2[j])
            j = j + 1
    
    def consume_rest(a, idx):
        nonlocal o
        while idx < len(a):
            o.append(a[idx])
            idx = idx + 1

    if i < len(arr1):
        consume_rest(arr1, i)
    
    if j < len(arr2):
        consume_rest(arr2, j)

    return o
    '''
    O(n+m) for lengths n=arr1, m=arr2, given that we go over the elements in each array at most once
    Uses O(n+m) space for output as well
    '''
'''
check_solution_simple(merge_sorted_arrays, args=[[], [4]], expected=[4])
check_solution_simple(merge_sorted_arrays, args=[[1], []], expected=[1])
check_solution_simple(merge_sorted_arrays, args=[[1], [4]], expected=[1,4])
check_solution_simple(merge_sorted_arrays, args=[[1,2], [3,4]], expected=[1,2,3,4])
check_solution_simple(merge_sorted_arrays, args=[[1,4], [2,3]], expected=[1,2,3,4])
check_solution_simple(merge_sorted_arrays, args=[[2,3], [1,4]], expected=[1,2,3,4])
check_solution_simple(merge_sorted_arrays, args=[[1,3,5], [2,4]], expected=[1,2,3,4,5])
check_solution_simple(merge_sorted_arrays, args=[[3], [1,5]], expected=[1,3,5])
'''

def is_subseq(s, t):
    '''
    392. Is Subsequence.

    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

    A subsequence of a string is a new string that is formed from the original string by 
    deleting some (can be none) of the characters without disturbing the relative positions 
    of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
    '''
    pass
    i = 0
    j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i = i + 1
        j = j + 1
    
    if i >= len(s):
        return True
    
    return False
    '''
    O(n+m) as we iterate at most through each char in s=n and t=m once
    '''

'''
check_solution_simple(is_subseq, args=["a", "a"], expected=True)
check_solution_simple(is_subseq, args=["a", "d"], expected=False)
check_solution_simple(is_subseq, args=["a", "ab"], expected=True)
check_solution_simple(is_subseq, args=["b", "ab"], expected=True)
check_solution_simple(is_subseq, args=["b", "abc"], expected=True)

check_solution_simple(is_subseq, args=["ab", "abc"], expected=True)
check_solution_simple(is_subseq, args=["bc", "abc"], expected=True)
check_solution_simple(is_subseq, args=["abc", "abc"], expected=True)
check_solution_simple(is_subseq, args=["ac", "abc"], expected=True)
check_solution_simple(is_subseq, args=["d", "abc"], expected=False)
check_solution_simple(is_subseq, args=["abcd", "abc"], expected=False)
check_solution_simple(is_subseq, args=["abd", "abc"], expected=False)

check_solution_simple(is_subseq, args=["ace", "abcde"], expected=True)
check_solution_simple(is_subseq, args=["aec", "abcde"], expected=False)
'''

# https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4592/
def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    '''
    Idea is to use double pointers to swap first/last and then work inwards
    '''
    
    i = 0
    j = len(s) - 1

    while i < j:
        t = s[i]
        s[i] = s[j]
        s[j] = t

        i = i + 1
        j = j - 1 

    # for testing
    return s

'''
check_solution_simple(reverseString, args=[list("")], expected=list(""))
check_solution_simple(reverseString, args=[list("a")], expected=list("a"))
check_solution_simple(reverseString, args=[list("ab")], expected=list("ba"))
check_solution_simple(reverseString, args=[list("abc")], expected=list("cba"))
check_solution_simple(reverseString, args=[list("abcd")], expected=list("dcba"))
'''

# https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4689/
def sortedSquares(nums: List[int]) -> List[int]:
    '''
    Idea is to start from either side of the array (front/end) and start
    adding the largest square value to the end of the output array, and moving
    the pointers inwards until we're done

    This works because the array is sorted, and the negative numbers, if any, at the beginning,
    will be larger than nums in the middle once squared. 
    '''
    o = [0] * len(nums)

    i = 0
    j = len(nums) - 1

    p = len(nums) - 1
    while p >= 0:
        left = abs(nums[i])
        right = abs(nums[j])

        if left > right:
            o[p] = left * left
            i = i + 1
        else:
            o[p] = right * right
            j = j - 1

        p = p - 1

    return o
    '''
    O(n) space and time
    '''

'''
check_solution_simple(sortedSquares, args=[[-4,1,10]], expected=[1,16,100])
check_solution_simple(sortedSquares, args=[[-4,0,10]], expected=[0,16,100])
check_solution_simple(sortedSquares, args=[[-4,-1,0,3,10]], expected=[0,1,9,16,100])
'''