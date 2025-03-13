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

# https://leetcode.com/problems/binary-tree-right-side-view/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        mval = math.inf
        prev = None

        def search(node):
            nonlocal mval, prev

            print(f"Search node: {node}")

            if not node:
                return

            search(node.left)

            print(f"\t node: {node.val}, prev: {(prev.val if prev else None)}")
            if prev:
                mval = min(mval, node.val - prev.val)

            prev = node 
            search(node.right)

        search(root)
        return mval 
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.getMinimumDifference

    t = [1,0,48,null,null,12,49]
    tr = GEN_TREE_FROM_LIST(t)
    print(f"Tree: {tr.__all__()}")

    print(sf(tr))

