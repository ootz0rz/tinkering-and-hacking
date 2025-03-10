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

# https://leetcode.com/problems/evaluate-division/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        # first, let's make sure no cycle exists
        visited = set()
        res = []
        used = set()
        def findPath(c):
            if c in visited:
                return False
            
            if c in used:
                return True

            visited.add(c)
            for n in graph[c]:
                if not findPath(n):
                    return False 
            visited.remove(c) # backtracking

            # add to our path and consume this node
            used.add(c)
            res.append(c)

            # we won't need the prereqs for this node again
            graph[c] = []
            
            return True

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
        args=[5, [[1,0],[2,0],[3,1],[3,2]]],
        expected=[0,2,1,3]
    )