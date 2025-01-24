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
Idea:

2 ptrs

i + i+n
Move to end until i+n+1 == Null
Remove i
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None: 
            # print("Empty input")
            return head
        
        start = ListNode(0, head)

        l1 = start
        l2 = head

        # try to move l2 up by +n
        while n > 0:
            n = n - 1
            l2 = l2.next

        # # valid?
        # if n > 0 or l2 is None:
        #     print(f"Too short, n:{n}, l2:{l2}")
        #     return head
        
        # print(f"Start: {l1}, Ptr 2: {l2}, n:{n}")

        # now move both pointers to end
        while l2 is not None:
            l1 = l1.next
            l2 = l2.next

        # print(f"End, l1:{l1}, l2:{l2}")

        # now we know that l1.next is our node to remove
        l1.next = l1.next.next

        # print(f"Removed: {start.next.__all__()}")
        return start.next 
        
        


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.removeNthFromEnd

    check_solution_simple(
        sf,
        args=[[1,5], 1],
        expected=[1],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )

    check_solution_simple(
        sf,
        args=[[1,2,3,4], 2],
        expected=[1,2,4],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )

    # check_solution_simple(
    #     sf,
    #     args=[[1,2,3,4], 2],
    #     expected=[1,2,4],
    #     input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
    #     output_transform_func=LN__LL_TO_ARRAY,
    # )