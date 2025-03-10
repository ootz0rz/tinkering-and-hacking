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

# https://leetcode.com/problems/course-schedule-ii/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # generate graph
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        res = []
        seen = set()
        used = set()

        def findPath(idx):
            if idx in seen:
                return False
            
            # we also want to track which nodes we've already used in an easy to check way
            # so we add a 2nd 'res' here, a used set
            if idx in used:
                return True
            
            # backtrack through subgraph
            seen.add(idx)
            for b in graph[idx]:
                if not findPath(b):
                    return False 
            seen.remove(idx)

            # at this point we can add this node to our result
            res.append(idx)

            # mark as used to avoid dupes later
            used.add(idx)

            return True

        # enumerate courses
        for idx in range(numCourses):
            if not findPath(idx):
                return []
        
        return res 


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.findOrder

    check_solution_simple(  
        sf,
        args=[1, []],
        expected=[0]
    )

    check_solution_simple(  
        sf,
        args=[2, [[1,0]]],
        expected=[0,1]
    )

    check_solution_simple(  
        sf,
        args=[4, [[1,0],[2,0],[3,1],[3,2]]],
        expected=[0,2,1,3]
    )