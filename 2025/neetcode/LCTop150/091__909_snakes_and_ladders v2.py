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

            n1 = num - 1 # convert to 0-based
            row = n - (n1 // n) - 1 # get row

            revrow = (row - n - 1)

            if revrow % 2 == 0:
                col = n1 - (revrow * n)
            else:
                col = n - (num - (revrow * n))

            return (row, col)
            # n1 = num - 1
            # row = n - (n1 // n)
            # r1 = row - 1

            # if row % 2 == 0:
            #     col = n1 - (r1 * n)
            # else:
            #     col = n - (num - (r1 * n))

            # return (r1, col)
        
        # now we can start to search
        def search(start, end):
            nonlocal n
            print(f"SEARCH {start} -> {end}")
            # if start == end:
            #     return 0
            
            # sx, sy = get_pos_for_number(start)
            # ex, ey = get_pos_for_number(end)
            # print(f"\t -> Coords: START[{sx}, {sy}] -> END[{ex}, {ey}]")

            q = deque([(start, 0)]) # [(num, numTurns to get here), ...]
            v = {} # num -> num turns to arrive here

            while len(q) > 0:
                node, turns = q.popleft()
                print(f"\tCheck node {node} at {turns}")

                if node == end:
                    # we're done
                    print(f"==> Reached End in {turns}")
                    return turns
                
                if node in v:
                    # cycle
                    print(f"==> CYCLE! {node} in {v}")
                    return -1
                
                # explore neighbours
                v[node] = turns
                for neighbour in range(node + 1, min(node + 6, end)+1):
                    # check if we need to follow the board or not before we Q our neighbour
                    nx, ny = get_pos_for_number(neighbour)
                    val = board[nx][ny]

                    print(f"\t\t Q Neighbor {neighbour}:{nx},{ny} = {val}")
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