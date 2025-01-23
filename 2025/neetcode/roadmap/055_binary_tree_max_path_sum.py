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

# https://neetcode.io/problems/binary-tree-maximum-path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Fucking stupid description.. turns out they don't care about the value of the path up to
current node, just the max set of left+node+right in the entire tree.... BAH
'''
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxval = root.val

        def findMax(node):
            nonlocal maxval

            if node is None:
                return 0
            
            nv = node.val

            left = max(0, findMax(node.left))
            right = max(0, findMax(node.right))

            maxval = max(maxval, nv + left + right)

            return nv + max(left, right)

        findMax(root)

        return maxval


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.diameterOfBinaryTree

