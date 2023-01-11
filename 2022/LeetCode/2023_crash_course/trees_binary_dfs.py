# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/707/traversals-trees-graphs/4686/

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


# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# ----------------------------------------------------------------------------------------------------------------------


# def minDepth(root: Optional[TreeNode]) -> int:
#     if root is None:
#         return 0

#     return 1 + min(minDepth(root.left), minDepth(root.right))


def minDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    if root.left == None and root.right == None:
        return 1  # leaf node

    d = 999999
    if root.left is not None:
        d = min(d, minDepth(root.left))

    if root.right is not None:
        d = min(d, minDepth(root.right))

    return 1 + d


def minDepth2(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    if root.left == None:
        return 1 + minDepth2(root.right)

    if root.right == None:
        return 1 + minDepth2(root.left)

    return 1 + min(minDepth2(root.left), minDepth2(root.right))


"""
# given

check_solution_simple(
    minDepth, args=[tree_from_binary_array([3, 9, 20, None, None, 15, 7])], expected=2
)
"""

# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/
# ----------------------------------------------------------------------------------------------------------------------


def maxAncestorDiff(root: Optional[TreeNode]) -> int:
    # print(f"root: {root}")
    if root is None:
        return 0

    def _diff(node, cmax, cmin):
        # print(f"node: {node}, max: {cmax}, min: {cmin}")
        if node is None:
            # print(f" -> node=None, diff={(cmax - cmin)}")
            return cmax - cmin

        cmax = max(cmax, node.val)
        cmin = min(cmin, node.val)

        leftmaxdiff = _diff(node.left, cmax, cmin)
        rightmaxdiff = _diff(node.right, cmax, cmin)

        return max(leftmaxdiff, rightmaxdiff)

    return _diff(root, root.val, root.val)


"""
# given

check_solution_simple(
    maxAncestorDiff,
    args=[tree_from_binary_array([8, 3, 10, 1, 6, None, None])],
    expected=7,
)
# """

# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/diameter-of-binary-tree/description/
# ----------------------------------------------------------------------------------------------------------------------


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    diameter = 0

    def compare_height(node):
        nonlocal diameter

        if node is None:
            return 0

        leftheight = compare_height(node.left)
        rightheight = compare_height(node.right)

        diameter = max(diameter, leftheight + rightheight)

        return max(leftheight, rightheight) + 1

    compare_height(root)

    return diameter


"""

check_solution_simple(
    diameterOfBinaryTree,
    args=[tree_from_binary_array([1, 2])],
    expected=1,
)

check_solution_simple(
    diameterOfBinaryTree,
    args=[tree_from_binary_array([1, 2, 3, 4, None, None, None])],
    expected=3,
)
"""
