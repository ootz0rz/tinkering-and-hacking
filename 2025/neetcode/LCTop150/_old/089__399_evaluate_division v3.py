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

# O(V+E) runtime
# O(V) memory
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {} # V -> [(E, weight), ...]

        # generate a graph from our equations and values
        # note that we generate it both ways from a -> b, and b -> a, with its respective costs
        for idx, (a, b) in enumerate(equations):
            val = values[idx]

            if not a in graph:
                graph[a] = {}
            
            if not b in graph:
                graph[b] = {}

            graph[a][b] = val
            graph[b][a] = 1/val
        
        print(f"Graph: {graph}")

        def find(start, end, cost=1):
            print(f"Find <{start} -> {end}>")
            if start == end:
                return cost
            
            q = deque([start]) # [node, ...]
            seen = {start: (None, 1)} # node: (node we got here from, cost)

            path = []
            while len(q) > 0:
                vert = q.popleft()

                if vert == end:
                    # we reached the end, so let's generate the path
                    # 
                    # we do this by appending this current element to our path, and then
                    # looking it up in the seen map
                    #
                    # we then check where we were 'referred' from in the seen map and then move our way up until we reach the end, None
                    
                    # NOTE that vert starts off here as just the node, but we don't need its cost since its the end node
                    #      so let's skip it
                    print(f"\tFound end<{end}> at vert<{vert}> -- seen: {seen}")
                    vert = seen[vert]
                    while vert[0] is not None:
                        print(f"\t\t -> VERT: {vert}")
                        path.append(vert)
                        vert = seen[vert[0]]
                    print(f"\t\tPath Generated: {path}")
                else:
                    # we haven't reached end, so Q up neighbours to search
                    print(f"\tQ neighbours: <{vert} -> {graph[vert]}")
                    for n in graph[vert].keys():
                        if not n in seen:
                            print(f" -> Adding n:{n}, cost: {graph[vert][n]}")
                            seen[n] = (vert, graph[vert][n]) # store where we came from
                            q.append(n)
            
            # at this point, we can just calculate the total cost of the path as the product
            # of the entire array
            #
            # since we're calculating product, order doesn't matter...but technicall our 
            # path is given as end -> ... -> start, so would usually reverse order
            print(f"Final Path: {path}")
            if len(path) == 0:
                cost = -1
            else:
                cost = 1
                for a in path: # we should technically reverse path, but doesn't matter here
                    cost *= a[1]
            
            return cost

        vals = []
        for a, b in queries:
            if (
                    not (a in graph) or 
                    not (b in graph)
                ):
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

    check_solution_simple(  
        sf,
        args=[[["a","b"],["c","d"]], [1.0,1.0], [["a","c"],["b","d"],["b","a"],["d","c"]]],
        expected=[-1.00000,-1.00000,1.00000,1.00000]
    )