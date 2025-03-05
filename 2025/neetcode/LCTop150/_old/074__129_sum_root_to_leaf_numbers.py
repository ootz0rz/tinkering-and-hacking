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

# https://leetcode.com/problems/path-sum/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []
        
        def findPaths(node, curpath=0):
            nonlocal nums

            if not node:
                return
            
            newpath = (curpath * 10) + node.val
            
            if not node.left and not node.right:
                # leaf node found
                nums.append(newpath)
                return
            
            findPaths(node.left, newpath)
            findPaths(node.right, newpath)

        findPaths(root)

        s = 0
        for n in nums:
            s += n

        return s
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.hasPathSum

    t = [1,2]
    tr = GEN_TREE_FROM_LIST(t)
    print(f"Tree: {tr.__all__()}")

    print(sf(tr, 1))

