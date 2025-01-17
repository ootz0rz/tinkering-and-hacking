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

# https://neetcode.io/problems/add-two-numbers

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1ptr = l1
        l2ptr = l2

        remainder = 0
        res = ListNode()
        head = res

        while l1ptr is not None or l2ptr is not None:
            l1val = 0 if l1ptr is None else l1ptr.val
            l2val = 0 if l2ptr is None else l2ptr.val

            oR = remainder
            newVal = l1val + l2val + remainder

            remainder = newVal // 10
            newVal = newVal % 10

            res.next = ListNode(newVal)

            # print(f"Add l:{l1ptr} + r:{l2ptr} + rem:{oR} => {res.next} ++ {remainder}")

            res = res.next
            l1ptr = None if l1ptr is None else l1ptr.next
            l2ptr = None if l2ptr is None else l2ptr.next

        # print(f"Remainder: {remainder}")
        if remainder > 0:
            res.next = ListNode(remainder)
        
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
        args=[[0], [0]],
        expected=[0],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )

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
        expected=[8,1],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )

    check_solution_simple(
        sf,
        args=[[1,2,3], [4,5,6]],
        expected=[5,7,9],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )

    check_solution_simple(
        sf,
        args=[[0,9], [9]],
        expected=[9,9],
        input_transform_func=TEST__ARRAY_TO_LL_AS_ARGS,
        output_transform_func=LN__LL_TO_ARRAY,
    )
