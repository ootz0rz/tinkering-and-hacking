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

# https://neetcode.io/problems/find-target-in-rotated-sorted-array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + ((right - left) // 2)

            em = nums[mid]
            er = nums[right]

            # continue search
            if em < er:
                # discard right side
                right = mid
            else:
                # discard left side
                left = mid + 1

        # nums[left] => min value

        # decide which half we should search within        
        pivot = left
        left = 0
        right = len(nums) - 1

        # we check the right side first, since pivot is going
        # to be the min value... it's just easier to use it
        # as the 'left' and then check until end of array to 
        # see if target is within those bounds
        if target >= nums[pivot] and target <= nums[-1]: # in right side?
            # discard left
            left = pivot
        else:
            # discard right
            right = pivot - 1
            
        # now search that remaining side for our target if possible
        while left <= right:
            mid = left + ((right - left) // 2)

            if nums[mid] == target:
                return mid
        
            if nums[mid] > target:
                # discard right
                right = mid - 1
            else:
                # discard left
                left = mid + 1

        return -1
        


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.search

    check_solution_simple(
        sf,
        args=[[3,4,5,6,1,2], 1],
        expected=4
    )

    check_solution_simple(
        sf,
        args=[[3,5,6,0,1,2], 4],
        expected=-1
    )

    check_solution_simple(
        sf,
        args=[[4,5,6,7,0,1,2], 5],
        expected=1
    )

    
