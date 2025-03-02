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

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # add sentinel start
        head = ListNode(0, head)

        # first, we find the -nth element
        ptr = head
        ptrLate = head

        # 2 ptrs, one ahead by n steps
        while n >= 0 and ptr:
            ptr = ptr.next
            n -= 1
        
        print(f"PTR: {ptr} and LATE: {ptrLate}")

        # move both along now
        while ptr:
            ptr = ptr.next
            ptrLate = ptrLate.next

        print(f"PTR: {ptr} and LATE: {ptrLate}")

        # ptrLate now represents the node right before the one we want to remove
        if ptrLate.next:
            ptrLate.next = ptrLate.next.next

        return head.next

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
        args=[[1,2,3,4,5], 2],
        expected=[1,2,3,5],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )

    check_solution_simple(
        sf,
        args=[[1,2], 1],
        expected=[1],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )

    check_solution_simple(
        sf,
        args=[[1], 1],
        expected=[],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )