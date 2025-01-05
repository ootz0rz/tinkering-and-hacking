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

'''
WATCH VIDEO ?? https://neetcode.io/problems/products-of-array-discluding-self
https://leetcode.com/problems/product-of-array-except-self/solutions/1342916/3-minute-read-mimicking-an-interview
'''
class Solution:
    '''
    Idea:

    Compute all postfix, store in `res` array. Then compute prefix, and multiply with values in res array to get final result.
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)

        res = [1] * l 

        # compute prefix first and store, easier
        prefix = 1
        for i in range(l):
            res[i] = prefix
            prefix = prefix * nums[i]

        # now postfix
        postfix = 1
        for i in range(l - 1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]

        return res

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.productExceptSelf

    # check_solution_simple(
    #     sf,
    #     args=[[1,2,3,4]],
    #     expected=[24,12,8,6]
    # )

    # check_solution_simple(
    #     sf,
    #     args=[[1,2,4,6]],
    #     expected=[48,24,12,8]
    # )

    check_solution_simple(
        sf,
        args=[[-1,1,0,-3,3]],
        expected=[0,0,9,0,0]
    )