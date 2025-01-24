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

# https://neetcode.io/problems/largest-rectangle-in-histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        rightBorder = [0] * n # num of blocks we can extend to the right, including ourselves
        leftBorder = [0] * n # ditto, to left

        # generate right borders
        stack = []
        for i in range(n - 1, -1, -1):
            h = heights[i]

            print(f"[0] height[{i}]: {h} -- {stack}")

            while stack and h <= stack[-1][0]:
                print(f"\t h:{h} < {stack[-1][0]}")
                sh, si = stack.pop()

            print(f"[1] height[{i}]: {h} -- {stack}")

            if len(stack) == 0:
                # we can go towards the end of the array
                rightBorder[i] = n - i
                print(f"\t -> END rightBorder[{i}] = {rightBorder[i]}")
            else:
                # we can only go up to the last element in stack
                rightBorder[i] = stack[-1][1] - i
                print(f"\t -> CALC rightBorder[{i}] = {rightBorder[i]}")
            
            # add ourselves and move on
            stack.append((h, i))
        
        print("Right Border: ", rightBorder)

        print()
        print("-" * 10)
        print()

        # generate left borders
        stack = []
        for i in range(n):
            h = heights[i]

            print("")
            print(f"[0] height[{i}]: {h} -- {stack}")

            while stack and h <= stack[-1][0]:
                print(f"\t h:{h} < {stack[-1][0]}")
                sh, si = stack.pop()

            print(f"[1] height[{i}]: {h} -- {stack}")

            if len(stack) == 0:
                # we can go towards the beginning of the array
                leftBorder[i] = i + 1
                print(f"\t -> END leftBorder[{i}] = {leftBorder[i]}")
            else:
                # we can only go up to the last element in stack
                leftBorder[i] = i - stack[-1][1]
                print(f"\t -> CALC leftBorder[{i}] = {leftBorder[i]}")
            
            # add ourselves and move on
            stack.append((h, i))
        
        print("Left Border: ", leftBorder)

        # finally do one last pass, where we calculate the total possible area at any given index
        # and track the largest one
        maxArea = 0
        for i, h in enumerate(heights):
            area = (leftBorder[i] * h) + (rightBorder[i] * h) - h
            area = h * (leftBorder[i] + rightBorder[i] - 1)

            print(f"area: {area} > maxArea: {maxArea}")

            maxArea = max(maxArea, area)

        return maxArea


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.largestRectangleArea

    check_solution_simple(
        sf,
        args=[[2,2,2]],
        expected=6
    )

    check_solution_simple(
        sf,
        args=[[2,1,5,6,2,3]],
        expected=10
    )