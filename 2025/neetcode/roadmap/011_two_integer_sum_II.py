from typing import List
import collections
import itertools
import functools
import math
import string
import random
import bisect
import re
import operator
import heapq
import queue

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

# https://neetcode.io/problems/two-integer-sum-ii
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
'''
Since sorted, we can start on either end of the array i=0, j=n-1...and then depending on if we're bigger than target (dec j) or smaller (inc i) and eventually find two target vals

We can also make sure i strictly < j to keep two independent vals.

If we really wanted, could binary search this too... 

NOTE NOTE NOTE: Result should be 1-indexed... derp
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            ei = numbers[i]
            ej = numbers[j]

            sum = ei + ej

            if sum == target:
                return [i + 1, j + 1]
            
            if sum > target:
                j = j - 1
            else:
                i = i + 1
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.isPalindrome

    check_solution_simple(
        sf,
        args=[[2,7,11,15], 9],
        expected=[1,2]
    )

    check_solution_simple(
        sf,
        args=[[2,3,4], 6],
        expected=[1,3]
    )

    check_solution_simple(
        sf,
        args=[[-1,0], -1],
        expected=[1,2]
    )