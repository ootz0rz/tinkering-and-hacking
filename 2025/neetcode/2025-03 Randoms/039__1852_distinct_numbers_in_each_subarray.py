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

class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        i = 0
        j = 0

        freq = defaultdict(int)

        # init with first k elements
        while (j - i) != k:
            e = nums[j]

            freq[e] += 1

            j += 1

        o = []
        while i <= j and j < len(nums):
            o.append(len(freq))

            freq[nums[i]] -= 1
            if freq[nums[i]] == 0:
                del freq[nums[i]]
            
            i += 1

            freq[nums[j]] += 1

            j += 1

        o.append(len(freq))
        print(f"o: {o}")

        return o

            
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.distinctNumbers

    check_solution_simple(
        sf,
        args=[[1,2,3,2,2,1,3], 3],
        expected=[3,2,2,2,3],
    )
