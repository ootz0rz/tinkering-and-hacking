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

# https://neetcode.io/problems/kth-smallest-integer-in-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        res = None

        # by doing in-order-traversal, we know we're going to go 
        # all the way down the left side first to the "smallest" element
        # 
        # then because this is a BST, as we unravel the stack, we're going
        # to the next largest element onwards
        def iot(node):
            nonlocal count, res

            if node is None:
                return
            
            iot(node.left)

            count = count - 1
            if count == 0:
                res = node.val
                return
            
            iot(node.right)

        iot(root)
            
        return res


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.diameterOfBinaryTree

