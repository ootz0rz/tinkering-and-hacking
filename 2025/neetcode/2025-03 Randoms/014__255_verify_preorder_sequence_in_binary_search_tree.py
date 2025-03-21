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

# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        
        pass


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.verifyPreorder

    check_solution_simple(
        sf,
        args=[[5,2,1,3,6]], 
        expected=True,
    )

    check_solution_simple(
        sf,
        args=[[5,2,6,1,3]], 
        expected=False,
    )
