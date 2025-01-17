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

# ------------ ListNode
# stupid...but works
import sys, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from LinkedList import *
# ------------ ListNode

# https://neetcode.io/problems/copy-linked-list-with-random-pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/description/

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

'''
Idea:

First pass; start creating copy of the main list
2nd pass of copy, add in the random pointers

We keep the random pointers in a dict, oldNode -> (newIdx, newNode)
'''
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        origNode = head
        origToClone = {None: None}

        # generate new nodes, and create a mapping
        while origNode is not None:
            clone = Node(origNode.val)
            origToClone[origNode] = clone
            origNode = origNode.next

        # now iterate through again, and set up linking + iteration
        origNode = head
        # res = Node(0)

        while origNode is not None:
            clonedNode = origToClone[origNode]
            clonedNext = origToClone[origNode.next]
            clonedRand = origToClone[origNode.random]

            clonedNode.next = clonedNext
            clonedNode.random = clonedRand

            origNode = origNode.next

        return origToClone[head]
            

        


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.copyRandomList

    # check_solution_simple(
    #     sf,
    #     args=[[1,5], 1],
    #     expected=[1],
    #     input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
    #     output_transform_func=LN__LL_TO_ARRAY,
    # )

    # check_solution_simple(
    #     sf,
    #     args=[[1,2,3,4], 2],
    #     expected=[1,2,4],
    #     input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
    #     output_transform_func=LN__LL_TO_ARRAY,
    # )

    # check_solution_simple(
    #     sf,
    #     args=[[1,2,3,4], 2],
    #     expected=[1,2,4],
    #     input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
    #     output_transform_func=LN__LL_TO_ARRAY,
    # )