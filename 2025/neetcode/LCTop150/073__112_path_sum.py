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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, t):
            if node is None:
                return False
            
            if node.val == t and not node.left and not node.right:
                return True
            
            tv = t - node.val            
            return dfs(node.left, tv) or dfs(node.right, tv)
        
        def findbfs():
            nonlocal root, targetSum

            if root is None:
                return False

            q = []
            q.append((root, targetSum - root.val))

            while len(q) > 0:
                node, tv = q.pop()

                if tv == 0 and not node.left and not node.right:
                    return True
                
                if node.right:
                    q.append((node.right, tv - node.right.val))
                
                if node.left:
                    q.append((node.left, tv - node.left.val))

            return False

        #return dfs(root, targetSum)
        return findbfs()
        

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

