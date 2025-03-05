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

# from BinaryTree import *
# ------------ BinaryTree

# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

'''
Idea:

Use BFS iteratively to go level by level, and assign the right elements
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        q = deque([root])

        while len(q) > 0:            
            n = len(q)
            
            # the idea is we pop the left-most element, set its "right" to the new beginning
            # of our queue, and then add our children
            #
            # then we just iterate through the queue until we hit the end of the number of 
            # children from that level given by n above
            for i in range(n):
                e = q.popleft()

                # this check is key; we want to make sure we don't start adding the next level as "right" nodes
                if i < n -1:
                    e.next = q[0]

                # add our children
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)

        return root
            
            


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.isSymmetric

