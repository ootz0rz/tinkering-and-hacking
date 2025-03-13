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

# https://leetcode.com/problems/clone-graph/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return f"<{self.val}, n:{len(self.neighbors)}>"

# O(V + E) runtime
# O(V) memory, O(H) stack (height of graph)
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        nodemap = {} # old node -> new node

        def deepClone(n):
            nonlocal nodemap
            
            if not n in nodemap:
                # create the clone
                nodemap[n] = Node(n.val)

                # populate neighbors
                nList = []
                for e in n.neighbors:
                    nList.append(deepClone(e))
                
                nodemap[n].neighbors = nList
            
            return nodemap[n]
                
        return deepClone(node)
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.cloneGraph

    n1 = Node(0)
    n2 = Node(1)
    n3 = Node(2)
    n4 = Node(3)

    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    check_solution_simple(  
        sf,
        args=[n1],
        expected=n1
    )