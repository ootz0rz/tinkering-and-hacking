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

from BinaryTree import *
# ------------ BinaryTree

# https://leetcode.com/problems/flip-equivalent-binary-trees/description/

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # print(f"Check: root1.val={root1.val if root1 else root1}, root2.val={root2.val if root2 else root2}")
        if root1 is None and root2 is None:
            # print(f"\t => Both None: True")
            return True
        
        if root1 is None or root2 is None:
            # print(f"\t => One None: False")
            return False
        
        if root1.val != root2.val:
            # print(f"\t => Not Same Vals: False")
            return False

        # print(f"Compare R1.LEFT:[{root1.left}]=R2.RIGHT:[{root2.right}], R1.RIGHT:[{root1.right}]=R2.LEFT:{root2.left}")
        return (
            # flip
            (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
            or 
            # no flip
            (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right))
        )


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.flipEquiv

    check_solution_simple(
        sf,
        args=[[1,2,3,4,5,6,null,null,null,7,8], [1,3,2,null,6,4,5,null,null,null,null,8,7]],
        expected=True,
        input_transform_func=TEST__ARRAY_TO_TN_AS_ARGS
    )

