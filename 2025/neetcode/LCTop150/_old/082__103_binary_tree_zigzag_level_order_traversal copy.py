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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        q = deque([root])

        o = []
        n = 0
        while len(q) > 0:
            
            vals = []
            for _ in range(len(q)):
                e = q.popleft()

                if n % 2 == 0:
                    vals.append(e.val)
                else:
                    vals.insert(0, e.val) # could also use a deque for this to appendleft 

                if e.left:
                    q.append(e.left)

                if e.right:
                    q.append(e.right)

            o.append(vals)

            n += 1
        
        return o
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.rightSideView

    t = [1,2,3,None,5,None,4]
    tr = GEN_TREE_FROM_LIST(t)
    print(f"Tree: {tr.__all__()}")

    print(sf(tr))

