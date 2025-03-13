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

# given a square ID number, return the coords to us
def get_pos_for_number(num, n):
    r = (num - 1) // n
    c = (num - 1) % n
    if r % 2:
        c = n - 1 - c
    return (r, c)

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        global EMPTY
        
        n = len(board)
        
        # just to make the math easier, we'll reverse the board
        board.reverse()
        
        # now we can start to search
        def search(start, end):
            nonlocal n
            # print(f"SEARCH {start} -> {end}")
            # if start == end:
            #     return 0
            
            # sx, sy = get_pos_for_number(start)
            # ex, ey = get_pos_for_number(end)
            # print(f"\t -> Coords: START[{sx}, {sy}] -> END[{ex}, {ey}]")

            q = deque([(start, 0)]) # [(num, numTurns to get here), ...]
            
            v = defaultdict(lambda: -1)

            while len(q) > 0:
                node, turns = q.popleft()
                # print(f"\tCheck node {node} at {turns}")

                if node == end:
                    # we're done
                    # print(f"==> Reached End in {turns}")
                    return turns
                
                if node in v:
                    # skip
                    # print(f"==> Skip {node}")
                    continue
                
                # explore neighbours
                v[node] = turns
                for neighbour in range(node + 1, min(node + 6, end)+1):
                    # check if we need to follow the board or not before we Q our neighbour
                    nx, ny = get_pos_for_number(neighbour, n)
                    val = board[nx][ny]

                    # print(f"\t\t Q Neighbor {neighbour}:{nx},{ny} = {val}")
                    if val == -1:
                        q.append((neighbour, turns + 1))
                    else:
                        q.append((board[nx][ny], turns + 1))

            return -1
        
        return search(1, n*n)
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.snakesAndLadders

    check_solution_simple(get_pos_for_number, args=[1, 2], expected=(0, 0))
    check_solution_simple(get_pos_for_number, args=[2, 2], expected=(0, 1))
    check_solution_simple(get_pos_for_number, args=[3, 2], expected=(1, 1))
    check_solution_simple(get_pos_for_number, args=[4, 2], expected=(1, 0))

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