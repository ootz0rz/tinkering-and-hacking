# https://leetcode.com/problems/subtree-of-another-tree/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        L = ""
        if self.left is not None:
            L = f"L[{self.left}]"

        R = ""
        if self.right is not None:
            R = f"R[{self.right}]"

        A = ""
        if len(L) > 0 or len(R) > 0:
            A = " "
            if len(L) > 0 and len(R) > 0:
                A = f"{A}{L} {R}"
            else:
                A = f"{A}{L}{R}"

        return f"<{self.val}{A}>"

    def __str__(self) -> str:
        # return str(self.val)
        return self.__repr__()


def GEN_TREE_FROM_LIST(L):
    n = len(L)
    if n == 0:
        return None

    def gen(idx: int = 0) -> "TreeNode":
        if idx >= n or L[idx] is None:
            return None

        node = TreeNode(L[idx])
        node.left = gen(2 * idx + 1)
        node.right = gen(2 * idx + 2)

        return node

    return gen()


def explore_match(root, subRoot):
    if root is None or subRoot is None:
        return False

    qR = [root]
    qS = [subRoot]

    while len(qR) > 0 and len(qS) > 0:
        cR = qR.pop(0)
        cS = qS.pop(0)

        if (cR is not None and cS is not None) and cR.val == cS.val:
            # explore rest
            qR.append(cR.left)
            qR.append(cR.right)

            qS.append(cS.left)
            qS.append(cS.right)
        elif cR is None and cS is None:
            continue
        else:
            return False

    # print(f"explore: qs={qS} qr={qR} => {(len(qS) == 0 and len(qR) == 0)}")
    return len(qS) == 0 and len(qR) == 0


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None or subRoot is None:
            return False

        R = [root]

        nR = len(R)
        while len(R) > 0:

            # print(f" -> R[{nR}]: {R}")

            i = 0
            while i < nR:
                # print(f" \t -> R[{i} < {nR}={(i < nR)}]: {R}")
                cR = R.pop(0)

                if cR.val == subRoot.val:
                    # we have a starter match so explore and exit if the same
                    if explore_match(cR, subRoot):
                        return True

                # no match yet... explore the rest
                if cR.left is not None:
                    R.append(cR.left)

                if cR.right is not None:
                    R.append(cR.right)

                i = i + 1

            nR = len(R)

        return False


if __name__ == "__main__":
    s = Solution()

    def checkSolution(root, subRoot, expected, msg="Expected `{0}` but got `{1}`"):
        print(f"--- subRoot:{subRoot} in root:{root}?")
        rr = GEN_TREE_FROM_LIST(root)
        rs = GEN_TREE_FROM_LIST(subRoot)
        r = s.isSubtree(rr, rs)

        print(f"{rs}\nin\n{rr}? {r}")
        assert r == expected, msg.format(expected, r)

    # checkSolution(root=[3, 4, 5, 1, 2], subRoot=[4, 1, 2], expected=True)

    # checkSolution(
    #     root=[3, 4, 5, 1, 2, None, None, None, None, 0],
    #     subRoot=[4, 1, 2],
    #     expected=False,
    # )
    checkSolution(
        root=[3, 4, 5, 1, 2],
        subRoot=[4, 1, None, None, 2],
        expected=False,
    )
