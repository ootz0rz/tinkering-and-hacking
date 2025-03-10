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

# https://leetcode.com/problems/snakes-and-ladders/?envType=study-plan-v2&envId=top-interview-150

EMPTY = -1
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        global EMPTY
        
        n = len(board)

        # given a square ID number, return the coords to us
        def get_pos_for_number(num):
            nonlocal n
            n1 = num - 1
            row = n1 // n

            if row % 2 == 0:
                col = n1 - (row * n)
            else:
                col = n - (num - (row * n))

            return (row, col)
        
        # now we can start to search
        v = set()
        def search(start, end, num_turns=0):
            nonlocal n
            print(f"SEARCH {start} -> {end} = {num_turns}")
            if start == end:
                return num_turns
            
            sx, sy = get_pos_for_number(start)
            ex, ey = get_pos_for_number(end)
            print(f"\t -> Coords: START[{sx}, {sy}] -> END[{ex}, {ey}]")

            # search our neighbors...
            if start in v:
                return -1 # invalid cycle
            
            v.add(start)
            minTurns = n * n
            for node in range(start + 1, min(start + 6, end)+1):
                r = search(node, end, num_turns + 1)
                if r == -1:
                    return -1
                
                minTurns = min(r, minTurns)
            v.remove(start)

            return minTurns
        
        return search(1, n*n, 0)
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.snakesAndLadders

    check_solution_simple(  
        sf,
        args=[[[-1,-1],[-1,-1]]],
        expected=1
    )

    check_solution_simple(  
        sf,
        args=[[[-1,-1],[-1,3]]],
        expected=1
    )

    check_solution_simple(  
        sf,
        args=[[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]],
        expected=4
    )