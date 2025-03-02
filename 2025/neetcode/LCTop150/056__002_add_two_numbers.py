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

# https://leetcode.com/problems/add-two-numbers/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2

        res = ListNode()
        head = res

        carry = 0
        while p1 is not None or p2 is not None:
            v1 = p1.val if p1 is not None else 0
            v2 = p2.val if p2 is not None else 0

            newVal = v1 + v2 + carry

            carry = newVal // 10
            newVal = newVal % 10

            res.next = ListNode(val=newVal)
            res = res.next

            if p1:
                p1 = p1.next
            
            if p2:
                p2 = p2.next

        if carry != 0:
            res.next = ListNode(val=carry)

        return head.next

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.addTwoNumbers

    check_solution_simple(
        sf,
        args=[[1], [1]],
        expected=[2],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )
    
    check_solution_simple(
        sf,
        args=[[9], [9]],
        expected=[8, 1],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )