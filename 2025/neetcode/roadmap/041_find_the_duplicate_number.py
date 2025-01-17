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

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

# ------------ ListNode
# stupid...but works
import sys, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from LinkedList import *
# ------------ ListNode

# https://neetcode.io/problems/find-duplicate-integer

'''
Since numbers are [0,n], we can mark the number as its value-1 as index, and negate the value there in nums
If we encounter it again and its already negative, we know its a dupe
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for e in nums:
            idx = abs(e) - 1

            if nums[idx] < 0:
                return abs(e)
            
            nums[idx] *= -1
        return -1


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.findDuplicate

    check_solution_simple(
        sf,
        args=[[1,2,3,1]],
        expected=1,
        # input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        # output_transform_func=LN__LL_TO_ARRAY,
    )

    check_solution_simple(
        sf,
        args=[[1,3,4,2,2]],
        expected=2,
        # input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        # output_transform_func=LN__LL_TO_ARRAY,
    )