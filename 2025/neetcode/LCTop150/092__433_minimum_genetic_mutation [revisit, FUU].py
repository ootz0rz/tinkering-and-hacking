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

# https://leetcode.com/problems/minimum-genetic-mutation/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        bankset = set(bank)

        q = deque([(startGene, 0)])
        visited = set()

        while len(q) > 0:
            node, steps = q.popleft()
            if node == endGene:
                return steps
            
            for m in "ACGT":
                for i in range(len(startGene)):
                    # generate neighbours
                    n = startGene[:i] + m + startGene[i+1:]

                    if (n in visited) or (not n in bankset):
                        continue 

                    visited.add(n)
                    q.append((n, steps + 1))
        
        return -1
                    


        

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