from typing import List, Optional, Self, Set, Dict
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

# https://leetcode.com/problems/combination-sum/?envType=study-plan-v2&envId=top-interview-150

_DIR = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        global _DIR 
        n = len(board)
        m = len(board[0])
        
        def search(x, y, remainder):
            nonlocal board, word
            print(f"SEARCH {x},{y},{remainder}")
            
            if len(remainder) == 0: # must check this first
                print(f" => FINISHED")
                return True
            
            if x < 0 or x >= n or y < 0 or y >= m:
                print(f" => INVALID COORDS {x},{y}")
                return False # invalid coords
            
            if board[x][y] != remainder[0]:
                print(f" => INVALID LETTER board:{board[x][y]} remainder:{remainder}")
                return False # invalid path
            
            board[x][y] = "-"

            ret = False
            for r, c in _DIR:
                xr = x + r 
                yc = y + c 

                # search rest
                ret = search(xr, yc, remainder[1:])
                if ret:
                    # return True
                    break # we break so we can cleanup board below
                
            board[x][y] = remainder[0] # avoid side effects

            return ret 

        for r, row in enumerate(board):
            for c, cell in enumerate(board[r]):
                s = search(r, c, word)
                print(f"SEARCH[{r}]{c}] = {s}")
                if s:
                    return True
        
        return False

        


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.exist

    b = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    check_solution_simple(  
        sf,
        args=[b, "ABCCED"],
        expected=True
    )

    b = [["A"]]
    check_solution_simple(  
        sf,
        args=[b, "A"],
        expected=True
    )