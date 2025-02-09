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

# https://neetcode.io/problems/kth-largest-integer-in-a-stream

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums

        heapq.heapify(nums)

        self._cleanup()

    def _cleanup(self):
        while len(self.arr) > self.k:
            heapq.heappop(self.arr)

    def add(self, val: int) -> int:
        # add to end
        heapq.heappush(self.arr, val)

        self._cleanup()

        # return top of heap?
        return self.arr[0]


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = KthLargest(3, [1, 2, 3, 3])
    sf = s.add

    check_solution_simple(sf, args=[3], expected=3)
    check_solution_simple(sf, args=[5], expected=3)
    check_solution_simple(sf, args=[6], expected=3)
    check_solution_simple(sf, args=[7], expected=5)
    check_solution_simple(sf, args=[8], expected=6)