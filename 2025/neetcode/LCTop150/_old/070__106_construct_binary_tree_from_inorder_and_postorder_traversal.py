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

# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
INORDER:

left, root, right 

POSTORDER

left, right, root
'''
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        postIdx = len(postorder) - 1

        # the trick here is that since we're given post-order, we keep 
        # building the right-most subtree first as long as possible,
        # so that way we can simply pop/traverse one element at a time;
        # from the end to beginning of postorder to get our root element
        # at each stage
        def build(ino):
            nonlocal postIdx
            if len(ino) == 0 or len(postorder) == 0:
                return None
            
            # instead of popping, we can track idx
            #rv = postorder.pop()
            rv = postorder[postIdx]
            postIdx -= 1

            root = TreeNode(rv)

            # find rv in ino
            idx = ino.index(rv)

            root.right = build(
                ino[idx+1:]
            )

            root.left = build(
                ino[:idx]
            )

            return root

        return build(inorder)


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.isSymmetric

