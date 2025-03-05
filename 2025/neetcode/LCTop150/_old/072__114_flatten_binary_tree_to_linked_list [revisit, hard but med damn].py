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

# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        print(root.__all__())

        # we know we have to do a preorder traversal at some point...
        # so start with that
        def f(node):
            if not node:
                return None
            
            if not node.left and not node.right:
                return node # reached leaf node
            
            leftEnd = f(node.left)
            rightEnd = f(node.right)

            # if we had a left subtree, shuffle it to the right
            if leftEnd:
                leftEnd.right = node.right
                node.right = node.left 
                node.left = None 

            # return final leaf element
            if rightEnd:
                return rightEnd
            return leftEnd

        f(root)
        print(root.__all__())
        



if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.flatten

    t = [1,2,5,3,4,None,6]
    tr = GEN_TREE_FROM_LIST(t)
    print(f"Tree: {tr.__all__()}")

    sf(tr)

