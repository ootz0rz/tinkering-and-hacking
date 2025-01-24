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
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)

        prefix = [0] * l
        suffix = [0] * l
        res = [0] * l

        # init start and ends
        prefix[0] = suffix[l - 1] = 1

        # build prefix
        for i in range(1, l):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        # print('prefix', prefix)

        # build suffix, starting from 2nd-most right side, towards left
        # n-2 => 2nd most from right
        # -1 => because 'range' is non-inclusive towards stop idx
        # -1 => iterate in reverse
        for i in range(l - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]

        # print('suffix', suffix)

        # build result array
        for i in range(l):
            res[i] = prefix[i] * suffix[i]

        return res

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.productExceptSelf

    check_solution_simple(
        sf,
        args=[[1,2,4,6]],
        expected=[48,24,12,8]
    )