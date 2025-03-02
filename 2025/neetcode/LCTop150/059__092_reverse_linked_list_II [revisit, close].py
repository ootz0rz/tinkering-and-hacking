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

# https://leetcode.com/problems/reverse-linked-list-ii/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start = head
        c = head
        prev = None
        leftNode = None

        num = right - left + 1

        # move up to left side
        # NOTE: left is given as 1-based index
        while c and left > 1:
            leftNode = c # save 'previous'
            c = c.next
            left -= 1
            #print(f"Moved to c.next: {left}")

        # now we know that 'leftNode' is the node right before `left`, if any
        # we can now reverse the next right-left+1 number of nodes
        #print(f"Cur Left Node: {leftNode} numToReverse Max: {num}")
        rightEnd = leftNode.next if leftNode else None
        
        while c is not None and num > 0:
            # save next
            temp = c.next 

            # change our 'next' ptr to previous item
            c.next = prev
            
            # head to next item in list, by setting ourselves
            # as the new previous item... and then setting the
            # current pointer to the originally saved next in temp
            prev = c 
            c = temp

            num -= 1

        # stitch together right side if need be
        if c and num == 0 and rightEnd:
            rightEnd.next = c

        # stitch together left side if need be
        if not leftNode:
            start = prev
        else:
            leftNode.next = prev

        return start

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.reverseBetween

    check_solution_simple(
        sf,
        args=[[1,2,3,4,5,6], 0, 6],
        expected=[6,5,4,3,2,1],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )

    check_solution_simple(
        sf,
        args=[[1,2,3,4,5,6], 2, 6],
        expected=[1,6,5,4,3,2],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )

    check_solution_simple(
        sf,
        args=[[1,2,3,4,5,6], 2, 4],
        expected=[1,4,3,2,5,6],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )