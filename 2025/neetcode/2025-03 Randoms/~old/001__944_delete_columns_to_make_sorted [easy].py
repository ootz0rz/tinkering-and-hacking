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

# https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        numToDel = 0

        for col in range(len(strs[0])):
            for row in range(len(strs) - 1):
                if strs[row][col] > strs[row+1][col]:
                    numToDel += 1
                    break 

        return numToDel


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
        args=[["cba","daf","ghi"]],
        expected=1,
    )