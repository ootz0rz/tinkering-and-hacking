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

# https://neetcode.io/problems/search-for-word

# valid directions
DIR = [
    [-1, 0],
    [0, -1],
    [1, 0],
    [0, 1]
]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        global DIR
        
        checked = []
        ni = len(board)
        nj = len(board[0])

        for _ in range(ni):
            checked.append([False] * nj)

        def dfs(i, j, pathlen):
            nonlocal checked

            # NOTE better to do all these checks OUTSIDE the loop, just check it on next iteration
            #      otherwise it gets a bit tricky with edge cases and shit
            #      
            #      Just let the iteration step go on first
            
            # if last letter matches, and we're at word length, we're done
            if pathlen == len(word):
                # print(f"{s} \tT - Found word! {pathlen}")
                return True
            
            # check bounds
            if i < 0 or i >= ni or j < 0 or j >= nj:
                return False
            
            # used?
            if checked[i][j]:
                return False
            
            # valid letter?
            if board[i][j] != word[pathlen]:
                return False
            
            # otherwise, search for next letter around where we're now at
            checked[i][j] = True

            for x,y in DIR:
                ix = i + x
                jy = j + y

                if dfs(ix, jy, pathlen + 1):
                    return True
                
            checked[i][j] = False 
            return False

        for i in range(0, len(board)):
            for j, je in enumerate(board[i]):
                if dfs(i, j, 0):
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

    board = [
        ["A","B","C","D"],
        ["S","A","A","T"],
        ["A","C","A","E"]
    ]

    check_solution_simple(
        sf,
        args=[board, "CAT"],
        expected=True
    )

    check_solution_simple(
        sf,
        args=[board, "BAT"],
        expected=False
    )

    board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    check_solution_simple(  
        sf,
        args=[board2, "ABCCED"],
        expected=True
    )