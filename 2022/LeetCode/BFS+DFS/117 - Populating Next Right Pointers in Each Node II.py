"""
# Definition for a Node.
"""
from typing import List


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self) -> str:
        L = ""
        if self.left is not None:
            L = f"L:[{self.left}]"

        R = ""
        if self.right is not None:
            R = f"R:[{self.right}]"

        N = ""
        if self.next is not None:
            N = f"{self.next.val}"

        A = ""
        if len(L) > 0 or len(R) > 0:
            A = ", "
            if len(L) > 0 and len(R) > 0:
                A = f"{A}{L} {R}"
            else:
                A = f"{A}{L}{R}"

        if len(N) > 0:
            A = f" → {N} {A}"

        return f"<{self.val}{A}>"

    def __str__(self) -> str:
        # return str(self.val)
        return self.__repr__()


def GEN_TREE_FROM_LIST(L):
    n = len(L)
    if n == 0:
        return None

    def gen(idx: int = 0) -> "Node":
        if idx >= n or L[idx] is None:
            return None

        node = Node(L[idx])
        node.left = gen(2 * idx + 1)
        node.right = gen(2 * idx + 2)

        return node

    return gen()


def TREE_TO_OUTPUT_LIST(node: "Node", out=[]) -> List:
    if node is None:
        return out

    # print(f"N: {node} out:{out}")

    next = node
    while next is not None:
        out.append(next.val)
        next = next.next

    out.append(None)

    # print(f"\t [1] N: {node} out:{out}")

    out = TREE_TO_OUTPUT_LIST(node.left, out)

    return out


import collections


class Solution:
    def connect(self, root: "Node") -> "Node":
        # print(f"Connect Root: {root}")
        if root is None:
            return None

        o = collections.deque()
        o.append(root)

        n = len(o)
        while n > 0:
            node = None
            i = 0

            while i < n:
                node = o.popleft()

                if node.left is not None:
                    o.put(node.left)

                if node.right is not None:
                    o.put(node.right)

                next = i + 1
                if next >= n:
                    break

                # print(f"Current Node: {node} next: {o[next]}")

                node.next = o[0]
                i = i + 1

            n = len(o)

        return root


if __name__ == "__main__":
    s = Solution()

    def checkSolution(root, expected, msg="Expected `{0}` but got `{1}`"):
        node = GEN_TREE_FROM_LIST(root)
        r = s.connect(node)

        rNode = TREE_TO_OUTPUT_LIST(r)

        assert rNode == expected, msg.format(expected, rNode)

    """
    print("\n\n------")
    print("Tree Gen")
    print("------")

    print(f"Empty: \n{(GEN_TREE_FROM_LIST([]))}")
    print(f"Single: \n{(GEN_TREE_FROM_LIST([10]))}")
    print(f"Simple: \n{(GEN_TREE_FROM_LIST([10, 20, 30]))}")
    print(f"Nulls: \n{(GEN_TREE_FROM_LIST([10, None, 30]))}")
    print(f"Sample: \n{(GEN_TREE_FROM_LIST([1,2,3,4,5,None,7]))}")

    print("\n\n------")
    print("Out Gen")
    print("------")
    n = GEN_TREE_FROM_LIST([1, 2, 3, 4, 5, None, 7])
    print(f"Sample: \n{n}\n{TREE_TO_OUTPUT_LIST(n, [])}")

    print()
    print()

    r = GEN_TREE_FROM_LIST([1, 2, 3, 4, 5, None, 7])
    r.left.next = r.right
    r.left.left.next = r.left.right
    r.left.right.next = r.right.right
    print(f"Sample Manually Connected: \n{r}\n{TREE_TO_OUTPUT_LIST(r, [])}")
    """

    print("\n\n------")
    print("TESTS")
    print("------")
    checkSolution(
        root=[],
        expected=[],
    )
    checkSolution(
        root=[1, 2, 3, 4, 5, None, 7],
        expected=[1, None, 2, 3, None, 4, 5, 7, None],
    )

    # checkSolution(
    #     isConnected=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
    #     expected=3,
    # )
