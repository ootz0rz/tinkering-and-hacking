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

# https://neetcode.io/problems/depth-of-binary-tree

'''
Traverse tree and swap left/right
'''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self._rec(root)

    def _rec(self, node: TreeNode) -> int:
        if node is None:
            return 0
        
        return max(
            1 + self._rec(node.left),
            1 + self._rec(node.right)
        )


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.invertTree

