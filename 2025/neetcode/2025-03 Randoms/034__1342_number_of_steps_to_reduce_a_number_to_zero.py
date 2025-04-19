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

# https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num <= 1:
            return num
        
        # self + remainder if not div by 2 + div by 2
        return 1 + num % 2 + self.numberOfSteps(num // 2)


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.numberOfSteps

    check_solution_simple(
        sf,
        args=[14],
        expected=6,
    )
