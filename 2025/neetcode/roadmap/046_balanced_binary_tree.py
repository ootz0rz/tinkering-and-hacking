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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        isBalanced = True
        
        def check_heights(node):
            nonlocal isBalanced

            if not isBalanced:
                # stop
                return 0 
            
            if node is None:
                return 0
            
            left = check_heights(node.left)
            right = check_heights(node.right)

            if abs(left - right) > 1:
                isBalanced = False
                return 0
            
            return 1 + max(left, right)
        
        check_heights(root)

        return isBalanced


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.diameterOfBinaryTree

