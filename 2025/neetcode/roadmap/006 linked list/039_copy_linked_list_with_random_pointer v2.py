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

Do it in a single pass by creating the node as needed, and filling in the val later
'''
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        origNode = head
        origToClone = {None: None}

        origNode = head
        while origNode is not None:
            if origNode not in origToClone:
                origToClone[origNode] = Node(0)

            if origNode.next not in origToClone:
                origToClone[origNode.next] = Node(0)

            if origNode.random not in origToClone:
                origToClone[origNode.random] = Node(0)

            clonedNode = origToClone[origNode]
            clonedNext = origToClone[origNode.next]
            clonedRand = origToClone[origNode.random]

            clonedNode.val = origNode.val
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