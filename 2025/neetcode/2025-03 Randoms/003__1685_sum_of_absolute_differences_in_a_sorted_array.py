from typing import List,Optional
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
import sys

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        l = len(nums)

        res = []

        prefix = [nums[0]] * l

        # build prefix arr
        for idx in range(1, l):
            prefix[idx] = nums[idx] + prefix[idx - 1]
        
        #import pprint; pprint.pprint(prefix)

        # generate final output
        for idx in range(l):
            n = nums[idx]

            leftMax = idx * n 
            rightMax = (l - idx - 1) * n

            leftSum = abs(leftMax - (prefix[idx-1] if 0 <= (idx-1) < l else 0))
            rightSum = abs(rightMax - (prefix[-1] - prefix[idx]))

            #print(f"\ti:{idx}={n}, max[{leftMax},{rightMax}], sum[{leftSum},{rightSum}] = {leftSum+rightSum}")

            res.append(leftSum + rightSum)

        return res 


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.getSumAbsoluteDifferences

    check_solution_simple(
        sf,
        args=[[1,4,6,8,10]],
        expected=[24,15,13,15,21],
    )