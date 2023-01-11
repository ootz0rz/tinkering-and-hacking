import pprint
from typing import List, Optional, Dict


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        if self.val is None:
            return ""

        L = ""
        R = ""

        if self.left is not None:
            L = f", L:{self.left}"
        if self.right is not None:
            R = f", R:{self.right}"

        if len(L) == 0 and len(R) == 0:
            return f"{self.val}"
        else:
            return f"<{self.val}{L}{R}>"

    def __repr__(self) -> str:
        return self.__str__()

    def __preorder(self, n):
        if n != None:
            print(n.val, end=" | ")
            self.__preorder(n.left)
            self.__preorder(n.right)
        else:
            print("None", end=" | ")

    def preorder(self):
        self.__preorder(self)


def __tree_from_binary_array(arr: List[any], i: int, n: int) -> TreeNode:
    # print(f"__tree_from_binary_array: {arr}, i:{i}, n:{n}")
    if arr is None or len(arr) == 0:
        # print(f" -> None [0]")
        return None

    node = None

    if i < n and arr[i] is not None:
        node = TreeNode(arr[i])
        # print(f" -> new node, val: {node.val}")
        # if node.val is None:
        #     print(f"\t --> node.val=None, i:{i}, arr[i]:{arr[i]}, arr:{arr}")

        node.left = __tree_from_binary_array(arr, 2 * i + 1, n)
        node.right = __tree_from_binary_array(arr, 2 * i + 2, n)
    # else:
    #     print(f" -> i >= n -> None [1]")

    return node


def tree_from_binary_array(arr: List[any]):
    # print(f"tree_from_binary_array: {arr}")
    return __tree_from_binary_array(arr, 0, len(arr))


"""
t = tree_from_binary_array([3, 9, 20, None, None, 15, 7])
print(t)
"""
