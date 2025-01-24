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

# https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree

'''
It's a BST.. so we know that a common descendent A of p, q will be defined as:

p.val <= A.val <= q.val 

We want to find the value A, with the greatest height h, such that A is still
an ancestor of p and q

Possible outcomes:

    - A splits p and q into each of it subtrees, in which case it's the LCA
    - A=p, or A=q, and the other element is in one of its subtrees
'''
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        res = None

        def LCA(node, p, q):
            nonlocal res
            if res is not None:
                return res
            
            if node is None:
                return None
            
            nv = node.val
            pv = p.val
            qv = q.val

            if pv > nv and qv > nv:
                # check right subtree
                LCA(node.right, p, q)
            elif pv < nv and qv < nv:
                # check left subtree
                LCA(node.left, p, q)
            else:
                # either nv == pv, nv == qv, or this is the split
                res = node
        
        LCA(root, p, q)
            
        return res 


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.diameterOfBinaryTree

