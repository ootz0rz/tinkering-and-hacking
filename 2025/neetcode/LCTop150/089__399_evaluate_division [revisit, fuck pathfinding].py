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
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {} # V -> [(E, weight), ...]

        for idx, (a, b) in enumerate(equations):
            val = values[idx]

            if not a in graph:
                graph[a] = []
            
            if not b in graph:
                graph[b] = []

            graph[a].append((b, val))
            graph[b].append((a, 1/val))
        
        print(f"Graph: {graph}")

        def find(start, end, cost=1):
            if start == end:
                return cost
            
            q = deque([start])
            seen = {start: (None, 1)}

            path = []
            while len(q) > 0:
                vert = q.popleft()

                if vert == end:
                    # generate path
                    while vert is not None:
                        path.append(vert)

                        if vert[0] is None:
                            break 
                        
                        vert = seen[vert[0]]

                for n, c in graph[start]:
                    if not n in seen:
                        seen[n] = (vert, cost) # store where we came from
                        q.append(n)
            
            cost = 1
            for a in path: # we should technically reverse path, but doesn't matter here
                cost *= a
            
            return cost

        vals = []
        for a, b in queries:
            if not (a in graph) or not (b in graph):
                vals.append(-1)
            else:
                vals.append(find(a, b))
        
        return vals
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.calcEquation

    check_solution_simple(  
        sf,
        args=[[["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]],
        expected=[6.00000,0.50000,-1.00000,1.00000,-1.00000]
    )