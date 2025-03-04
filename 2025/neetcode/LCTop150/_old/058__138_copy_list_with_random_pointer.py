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

Node = RandomNode

# https://leetcode.com/problems/copy-list-with-random-pointer/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        res = Node(0)
        newHead = res

        oldToNew = {} # map of head[i] to newHead[i]

        # first pass, copy nodes
        ptr = head
        while ptr is not None:
            res.next = Node(ptr.val)

            oldToNew[ptr] = res.next

            res = res.next
            ptr = ptr.next

        # second pass, copy randoms
        ptr = head
        while ptr is not None:
            newNode = oldToNew[ptr]

            if ptr.random is not None:
                newRandom = oldToNew[ptr.random]
                newNode.random = newRandom

            ptr = ptr.next

        return newHead.next


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.mergeTwoLists

    check_solution_simple(
        sf,
        args=[[1,2,4], [1,3,4]],
        expected=[1,1,2,3,4,4],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )