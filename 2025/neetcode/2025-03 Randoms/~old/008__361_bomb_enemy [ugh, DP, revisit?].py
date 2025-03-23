from typing import List,Optional
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
import sys

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

# https://leetcode.com/problems/bomb-enemy/

'''
Idea:

Scan through each position i,j in the grid. 

At each position we can calculate the number of potential hits in the respective
row/column.

Note that for any position along a row or column, with its ends marked as [a,b]:
    Assuming that there are no walls within the range [a,b], then the number of
    possible enemies is the same for any empty position in that range.
'''
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        ENEMY = "E"
        WALL = "W"
        EMPTY = "0"
        
        rows = len(grid)
        cols = len(grid[0])

        maxCount = 0

        curRowCount = 0
        curColCount = [0] * cols

        for row in range(rows):
            for col in range(cols):
                cell = grid[row][col]

                #print(f"Check Cell: {row},{col} = {cell}")

                # we are currently iterating along, lets calculate how many enemies are on
                # this row/col and keep it saved for use
                #
                # we do this either when we are first starting the row, and go until we hit 
                # a wall or the end
                #
                # or we do this when we previously hit a wall, and to until the end/next wall

                # NOTE: by iterating along one col at a time, we're traversing each row first
                if col == 0 or grid[row][col - 1] == WALL: # row reset?
                    #print(f"\t[0]RESET ROW START => {curRowCount}")
                    curRowCount = 0
                    # j = col
                    # while j < m and grid[row][j] != WALL:
                    for j in range(col, cols):
                        #print(f"\t\t -> RESET ROW CHECK {row},{j} = {grid[row][j]}")
                        if grid[row][j] == WALL:
                            break

                        if grid[row][j] == ENEMY:
                            curRowCount += 1
                        
                        # j += 1
                    #print(f"\t[1]RESET ROW END => {curRowCount}")

                # do we need to reset our column too?
                if row == 0 or grid[row - 1][col] == WALL:
                    #print(f"\t[0] RESET COL START[{row}] => {curColCount[col]}")
                    curColCount[col] = 0
                    # i = row 
                    # while i < n and grid[i][col] != WALL:
                    for i in range(row, rows):
                        #print(f"\t\t -> RESET COL CHECK {i},{col} = {grid[i][col]}")
                        if grid[i][col] == WALL:
                            break

                        if grid[i][col] == ENEMY:
                            curColCount[col] += 1

                        # i += 1
                    #print(f"\t[1] RESET COL END[{row}] => {curColCount[col]}")
                
                # finally, check if we should place a bomb
                if cell == EMPTY:
                    #print(f"\t\t => Update Max:{maxCount} to {(curRowCount + curColCount[col])}?")
                    maxCount = max(maxCount, curRowCount + curColCount[col])
                
        return maxCount

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.maxKilledEnemies

    check_solution_simple(
        sf,
        args=[[["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]],
        expected=3,
    )
