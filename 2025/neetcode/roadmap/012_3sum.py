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

# https://neetcode.io/problems/three-integer-sum
# https://leetcode.com/problems/3sum/description/
'''

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        L = len(nums)

        # sort first nlogn
        nums.sort()
        
        seen = set()

        res = []

        for cidx in range(L):
            e = nums[cidx]

            if e > 0:
                # we can't sum positive-only numbers to 0, so we can skip this part of the array onwards
                break

            if cidx > 0 and nums[cidx] == nums[cidx-1]:
                # skip values we've already processed
                continue

            # 2sum to find other values that add to -e
            i = cidx + 1
            j = L - 1

            target = -e

            while i < j:
                ei = nums[i]
                ej = nums[j]

                sum = ei + ej

                if sum == target:
                    res.append([e, ei, ej])
                
                if sum > target:
                    j = j - 1
                    # skip dupes
                    while nums[j] == nums[j+1] and i < j:
                        j = j - 1
                else:
                    i = i + 1
                    # skip dupes
                    while nums[i] == nums[i-1] and i < j:
                        i = i + 1

        return res
            

        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.threeSum

    check_solution_as_tuplesets(
        sf,
        args=[[0,0,0]],
        expected=[[0,0,0]]
    )

    check_solution_as_tuplesets(
        sf,
        args=[[0,1,1]],
        expected=[]
    )

    check_solution_as_tuplesets(
        sf,
        args=[[-1,0,1,2,-1,-4]],
        expected=[[-1,-1,2],[-1,0,1]]
    )