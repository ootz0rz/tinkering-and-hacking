# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/707/traversals-trees-graphs/4619/

import pprint
from typing import List, Optional, Dict

# stupid...but works
import sys, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from TestHarness import *

# setup

from trees_binary_base import *

"""
NOTE dfs is typically with recursion
but BFS easier iteratively with a queue
"""

# In general...
def print_all_nodes(root):
    from collections import deque

    queue = deque([root])
    while queue:
        nodes_in_current_level = len(queue)
        # do some logic here for the current level

        for _ in range(nodes_in_current_level):
            node = queue.popleft()

            # do some logic here on the current node
            print(node.val)

            # put the next level onto the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/deepest-leaves-sum/description/
# ----------------------------------------------------------------------------------------------------------------------


def deepestLeavesSum(root: Optional[TreeNode]) -> int:
    from collections import deque

    q = deque()
    q.append((root, 0))

    deepest_level = 0
    sum = 0
    while len(q) > 0:
        n, cdepth = q.popleft()

        # if we find a leaf node.. check the depth so far
        if n.left is None and n.right is None:
            # if we're deeper than the deepest we've encountered...
            if deepest_level < cdepth:
                # set new deepest level, and reset sum
                deepest_level = cdepth
                sum = n.val
            # otherwise if at same deepest level...
            elif cdepth == deepest_level:
                # keep adding to sum
                sum = sum + n.val

        else:
            if n.left is not None:
                q.append((n.left, cdepth + 1))

            if n.right is not None:
                q.append((n.right, cdepth + 1))

    return sum


"""
t1 = tree_from_binary_array([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])

check_solution_simple(
    deepestLeavesSum,
    args=[t1],
    expected=19,
)
"""

# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
# ----------------------------------------------------------------------------------------------------------------------


def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []

    from collections import deque

    q = deque()
    q.append((root, 0))

    ans = []

    while len(q) > 0:
        n, d = q.popleft()

        while len(ans) <= d:
            ans.append([])

        if d % 2 == 0:
            # left to right
            ans[d].append(n.val)
        else:
            # right to left
            ans[d].insert(0, n.val)

        if n.left is not None:
            q.append((n.left, d + 1))

        if n.right is not None:
            q.append((n.right, d + 1))

    return ans


# given
t1 = tree_from_binary_array([3, 9, 20, None, None, 15, 7])
check_solution_simple(zigzagLevelOrder, args=[t1], expected=[[3], [20, 9], [15, 7]])
