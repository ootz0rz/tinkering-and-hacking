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

#https://leetcode.com/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        lastIdx = -1
        runCost = 0
        total = 0

        for i in range(len(gas)):
            curCost = gas[i] - cost[i]
            runCost += curCost
            total += curCost

            if lastIdx == -1 and runCost >= 0:
                lastIdx = i

            if runCost < 0:
                lastIdx = -1
                runCost = 0
            
            #print(f"i: {i} -- cur:{curCost} run:{runCost} total:{total} lastIdx:{lastIdx}")
        
        return lastIdx if (total >= 0) else -1
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.canCompleteCircuit

    check_solution_simple(  
        sf,
        args=[[1,2,3,4,5], [3,4,5,1,2]],
        expected=3
    )

    check_solution_simple(  
        sf,
        args=[[2,3,4], [3,4,3]],
        expected=-1
    )

    check_solution_simple(  
        sf,
        args=[[3,1,1], [1,2,2]],
        expected=0
    )