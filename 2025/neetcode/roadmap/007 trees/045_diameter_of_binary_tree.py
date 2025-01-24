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

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

# ------------ BinaryTree
# stupid...but works
import sys, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from BinaryTree import *
# ------------ BinaryTree

# https://neetcode.io/problems/binary-tree-diameter

'''
Find longest length of left side, and longest of right side, add together...
'''

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def get_max_height(node):
            nonlocal diameter

            if node is None:
                return 0
            
            # get max height of each side
            left = get_max_height(node.left)
            right = get_max_height(node.right)

            # update diameter if need be
            diameter = max(
                diameter,
                left + right
            )

            # return the tallest side from whatever side we have here, plus ourselves
            return 1 + max(left, right)

        get_max_height(root)

        return diameter


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.diameterOfBinaryTree

