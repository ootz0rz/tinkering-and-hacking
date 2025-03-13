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

# https://leetcode.com/problems/kth-smallest-element-in-a-bst/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, gt, lt):
            if node is None:
                return True
            
            if node.val <= gt or node.val >= lt:
                return False
            
            return validate(node.left, gt, node.val) and validate(node.right, node.val, lt)
            
        return validate(root, -math.inf, math.inf)
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.isValidBST

    t = [2,1,3]
    tr = GEN_TREE_FROM_LIST(t)
    print(f"Tree: {tr.__all__()}")
    print(t, sf(tr))


    t = [5,1,4,null,null,3,6]
    tr = GEN_TREE_FROM_LIST(t)
    print(f"Tree: {tr.__all__()}")
    print(t, sf(tr))