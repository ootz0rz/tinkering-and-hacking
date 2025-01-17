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

# https://neetcode.io/problems/reorder-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Idea..

1) Find half-way mark
2) Reverse 2nd half
3) "zip" the two halves together
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return None
        
        if head.next is None:
            return head
        
        # print("HEAD: ", head.__all__())

        # find half way mark
        l1 = head
        l2 = head.next

        while l1 is not None and l2 is not None:
            l1 = l1.next

            if l2.next is None:
                break

            l2 = l2.next.next
        
        # print("Found half: ", l1.__all__())

        l2 = l1
        l1 = head

        # reverse 2nd half
        curNode = l2
        prev = None

        while curNode is not None:
            temp = curNode.next
            curNode.next = prev
            prev = curNode
            curNode = temp
        
        l2 = prev

        # print(f"Finished Reverse: ", l2.__all__())
        # print(f"Head: ", head.__all__())

        res = ListNode()
        start = res

        # print(f"RES: {res}, L1: {l1}, L2: {l2}")

        # zip
        while l2 is not None:
            if l1 == l2:
                res.next = l1
                # print(f"\t end L1: {l1} L2: {l2} | TL1: {tl1} TL2: {tl2} ||| {start.__all__()}")
                break

            tl1 = l1.next
            tl2 = l2.next 

            l1.next = l2
            res.next = l1

            res = l2

            # print(f"\t loop L1: {l1} L2: {l2} | TL1: {tl1} TL2: {tl2} ||| {start.__all__()}")

            l1 = tl1
            l2 = tl2
        
        head = start.next
        return start.next
        


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.reorderList

    check_solution_simple(
        sf,
        args=[[2,4,6,8]],
        expected=[2,8,4,6],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )

    check_solution_simple(
        sf,
        args=[[2,4,6,8,10]],
        expected=[2,10,4,8,6],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )