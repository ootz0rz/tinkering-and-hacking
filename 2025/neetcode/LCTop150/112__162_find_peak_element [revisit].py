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
    def findPeakElement(self, nums: List[int]) -> int:
        # CAN USE BINARY SEARCH HERE ONLY BECAUSE OF:
        # 1. two neighbouring elements are never the same
        # 2. elements outside the array are considered infinitely small
        pass 


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.findPeakElement

    check_solution_simple(
        sf,
        args=[[1,2,3,1]],
        expected=2,
    )