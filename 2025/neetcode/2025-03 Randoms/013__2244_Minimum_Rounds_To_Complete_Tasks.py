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

Sort

Find count of current number
'''
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks.sort()

        curNum = tasks[0]
        curCount = 0

        print(f"TASKS: {tasks}")

        def process(curCount):
            count2 = 0
            while curCount%3 != 0:
                curCount -= 2 
                count2 += 1

            if curCount < 2:
                return -1
            else:
                return count2 + curCount // 3

        finalCount = 0
        for t in tasks:
            if t == curNum:
                curCount += 1
            else:
                # reset, so lets process the count
                print(f"num[{curNum}]=count[{curCount}], finalCount: {finalCount}")

                r = process(curCount)
                if r == -1:
                    return -1
                
                finalCount += r 

                curCount = 1
                curNum = t
        
        r = process(curCount)
        if r == -1:
            return -1
        
        return finalCount + r


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