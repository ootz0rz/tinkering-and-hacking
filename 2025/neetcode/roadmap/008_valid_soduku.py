from typing import List
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

'''
https://neetcode.io/problems/valid-sudoku
'''
_BLANK = "."

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        global _BLANK
        
        xsets = {}
        ysets = {}
        blocksets = {}

        for x in range(len(board)):
            for y in range(len(board[x])):
                exy = board[x][y]

                if exy == _BLANK:
                    continue

                # y coord
                if not (y in ysets):
                    ysets[y] = set()

                if exy in ysets[y]:
                    return False
                
                ysets[y].add(exy)

                # x coord
                if not (x in xsets):
                    xsets[x] = set()

                if exy in xsets[x]:
                    return False
                
                xsets[x].add(exy)
                
                # block sets
                sqx = x // 3
                sqy = y // 3
                if not (sqx in blocksets):
                    blocksets[sqx] = {}
                
                if not (sqy in blocksets[sqx]):
                    blocksets[sqx][sqy] = set()

                if exy in blocksets[sqx][sqy]:
                    return False
                
                blocksets[sqx][sqy].add(exy)

        return True


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.isValidSudoku

    board = \
        [["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]
    check_solution_simple(
        sf,
        args=[board],
        expected=True
    )