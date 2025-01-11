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
    '''
    We can find the min value, and then treat it as 2 diff parts to binary search
    '''
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + ((right - left) // 2)

            em = nums[mid]
            er = nums[right]

            # some early exits
            if em == target:
                return mid
            
            if er == target:
                return right
            
            if nums[left] == target:
                return left

            # continue search
            if em < er:
                # discard right side
                right = mid
            else:
                # discard left side
                left = mid + 1

        # nums[left] => min value

        # decide which half we should search within
        if nums[0] <= target <= nums[left]:
            # search left
            right = left
            left = 0
        else:
            # search right
            right = len(nums) - 1

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

    
