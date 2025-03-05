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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        tn = None
        
        def find(node, pval, qval):
            nonlocal tn 

            if node is None:
                return False
        
            lm = node.val == pval or node.val == qval
            lf = find(node.left, pval, qval) 
            lr = find(node.right, pval, qval)

            # 3 cases:
            # root can be one of the vals, and we find other val in left or right
            # or
            # root is not a val, and we find in both left and right
            if (lm and lf) or (lm and lr) or (lf and lr):
                tn = node
            
            # if we find in any of the 3 cases, we return true for this path
            return lm or lf or lr
        
        find(root, p.val, q.val)
        return tn 
        

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

