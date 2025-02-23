from typing import List, Optional, Self
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

# https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150
'''
Idea: Sort, then for each index, 2sum with rest?
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # nlogn

        res = set()
        # n2
        for i,e in enumerate(nums):
            # skip dupes -- huge gains for very repetitive and large input arrays
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            LS = i + 1
            RS = len(nums) - 1

            target = -e
            while LS < RS:
                s = nums[LS] + nums[RS]

                if s == target:
                    res.add((e, nums[LS], nums[RS]))
                    LS += 1
                    RS -= 1
                    continue

                if s > target:
                    RS -= 1
                else:
                    LS += 1
        
        return list(res)

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.twoSum

    check_solution_simple(  
        sf,
        args=[[2,7,11,15], 9],
        expected=[1, 2]
    )
