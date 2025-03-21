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

# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/

'''
Idea:

Count freq of each task
See if they're possible

Always try to divide by 3 at a time to optimize
If we can't then there's two cases

Num % 3 == 0 -- we're good, div by 3 and move on
Num % 3 == 1 -- 2+(Num-4)//3
Num % 3 == 2 -- 1+(Num-2)//3 
'''
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = defaultdict(int)

        for t in tasks:
            d[t] += 1

        finalVal = 0
        for key in d:
            v = d[key]

            if v == 1:
                return -1 # invalid
            
            if v % 3 == 0:
                finalVal += v // 3
            elif v % 3 == 1:
                finalVal += 2 + ((v-4)//3)
            else:
                finalVal += 1 + ((v-2)//3)
        
        return finalVal


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.minimumRounds

    check_solution_simple(
        sf,
        args=[[2,2,3,3,2,4,4,4,4,4]], 
        expected=4,
    )

    check_solution_simple(
        sf,
        args=[[2,3,3]], 
        expected=-1,
    )

    check_solution_simple(
        sf,
        args=[[2]], 
        expected=-1,
    )