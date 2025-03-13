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
        
        # let's build the graph first
        # weight = value
        # a/b = weight
        # b/a = 1/weight
        for idx, val in enumerate(values):
            a, b = equations[idx]
            
            if not a in graph:
                graph[a] = {}
            if not b in graph:
                graph[b] = {}
            
            graph[a][b] = val # a/b
            graph[b][a] = 1 / val # b/a

        def search(start, end):
            # print(f"SEARCH[s:{start}, e:{end}, c:{cost}]")
            if start == end: 
                # print(f"\t{start}=={end} => {cost}")
                return 1
            
            # direct neighbour so we can just return the value here
            if end in graph[start]:
                # print(f"\t{end} in graph[{start}]={graph[start]} => {cost * graph[start][end]}")
                return graph[start][end]
            
            # BFS path search
            q = deque([start])

            # to generate out final path we need to recall the node and cost of the 
            # node pairing that brought us here in our visited set
            v = {start: (None, 1)} # visited: (referring node, cost [refer/visited])

            path = []
            while len(q) > 0:
                a = q.popleft()

                if a == end:
                    # generate path
                    refer = v[a]
                    while refer[0] is not None:
                        path.append(refer[1])
                        refer = v[refer[0]]
                    break
                
                # explore rest
                for b in graph[a]:
                    if not b in v:
                        v[b] = (a, graph[a][b])
                        q.append(b)

            if len(path) == 0:
                # no valid path found
                return -1
            
            finalCost = 1
            for p in path:
                finalCost *= p
            
            return finalCost

        # next we want to start processing queries and begin creating our output list
        res = []
        for a, b in queries:
            # invalid query, a or b doesn't exist in equations
            if not a in graph or not b in graph:
                res.append(-1)
                continue

            # otherwise we want to search for our match
            # print(f"Search: {a} -> {b}")
            r = search(a, b)
            # print(f"RES: {r}")
            res.append(r)

        return res
        

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

    check_solution_simple(  
        sf,
        args=[[["a","b"],["c","d"]], [1.0,1.0], [["a","c"],["b","d"],["b","a"],["d","c"]]],
        expected=[-1.00000,-1.00000,1.00000,1.00000]
    )