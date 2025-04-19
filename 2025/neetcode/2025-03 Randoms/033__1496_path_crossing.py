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

DIRS = {
    "N": (0, 1),
    "S": (0, -1),
    "E": (1, 0),
    "W": (-1, 0)
}
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        global DIRS
        v = set([(0,0)])

        curCoord = [0, 0]
        for dir in path:
            pdir = DIRS[dir]

            curCoord[0] += pdir[0]
            curCoord[1] += pdir[1]

            sc = tuple(curCoord)
            if sc in v:
                return True
            
            v.add(sc)
                 
        return False


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.isPathCrossing

    check_solution_simple(
        sf,
        args=["NNSWWEWSSESSWENNW"],
        expected=True,
    )
