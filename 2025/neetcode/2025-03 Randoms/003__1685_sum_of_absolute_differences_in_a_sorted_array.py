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
        pass


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.minDeletionSize

    check_solution_simple(
        sf,
        args=[[2,2,1]],
        expected=1,
    )