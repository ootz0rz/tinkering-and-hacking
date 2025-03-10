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

        visited = set()
        def search(start, end, cost):
            # print(f"SEARCH[s:{start}, e:{end}, c:{cost}]")
            if start == end: # start/end = 1
                # print(f"\t{start}=={end} => {cost}")
                return cost
            
            # direct neighbour so we can just return the value here
            if end in graph[start]:
                # print(f"\t{end} in graph[{start}]={graph[start]} => {cost * graph[start][end]}")
                return cost * graph[start][end]
            
            # look for neighbour in tree
            if start in visited:
                # print(f"\t{start} already visited {visited}")
                return -1
            
            visited.add(start)
            
            t = cost
            for n in graph[start]:
                t *= search(n, end, graph[start][n])

            visited.remove(start)
            
            # print(f"\t\t{a} -> {b} = t:{t}")
            return t

        # next we want to start processing queries and begin creating our output list
        res = []
        for a, b in queries:
            # invalid query, a or b doesn't exist in equations
            if not a in graph or not b in graph:
                res.append(-1)
                continue

            # otherwise we want to search for our match
            # print(f"Search: {a} -> {b}")
            r = search(a, b, 1)
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