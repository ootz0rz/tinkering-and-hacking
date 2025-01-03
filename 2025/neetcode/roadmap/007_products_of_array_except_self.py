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

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix = [nums[0]]
        suffix = [nums[-1]]
        res = []

        cur_idx = 0
        while cur_idx < len(nums):

            # build prefix as needed
            left = 0
            while left < cur_idx:
                L = nums[left]

                if len(prefix) - 1 < left:
                    prefix.append(prefix[-1] * L)

                print('[0] cur', cur_idx, 'left', left, 'L', L, 'prefix', prefix)
                left = left + 1

            # build suffix as needed
            right = len(nums) - 2
            while right > cur_idx:
                R = nums[right]

                if len(suffix) - 1 < right:
                    suffix.insert(0, suffix[0] * R)

                print('[1] cur', cur_idx, 'right', right, 'R', R, 'suffix', suffix)
                right = right - 1

            cur_idx = cur_idx + 1
        
        print('prefix', prefix)
        print('suffix', suffix)

        return []

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