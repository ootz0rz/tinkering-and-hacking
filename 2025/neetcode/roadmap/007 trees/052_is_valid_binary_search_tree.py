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

# https://neetcode.io/problems/count-good-nodes-in-binary-tree

'''
We're going to traverse and maintain upper/lower-bound values per stage

Cases:
    lowerbound=Null:
        ignore

    upperbound=Null:
        ignore

    nv <= lowerbound:
        False

    nv >= upperbound:
        False
    
    
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node, lowerBound, upperBound):
            if node is None:
                return True # vacuously true
            
            nv = node.val
            if (nv <= lowerBound) or (nv >= upperBound):
                return False
            
            return isValid(node.left, lowerBound, nv) and isValid(node.right, nv, upperBound)

        return isValid(root, float("-inf"), float("inf"))


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.diameterOfBinaryTree

