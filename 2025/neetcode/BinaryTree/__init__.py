from typing import List, Optional, Self

null = None

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val

        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"{self.val}"
    
    def __str__(self):
        return self.__repr__()
    
    def __all__(self):
        return f"[V: {self.val} L: {self.left if self.left is None else self.left.__all__()} R: {self.right if self.right is None else self.right.__all__()}]"

def GEN_TREE_FROM_LIST(L:List) -> "TreeNode":
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


def TREE_TO_OUTPUT_LIST(node: "TreeNode", out:List=[]) -> List:
    if node is None:
        return out

    # print(f"N: {node} out:{out}")
    
    next_ = node
    while next_ is not None:
        out.append(next_.val)
        next_ = next_.next

    out.append(None)

    # print(f"\t [1] N: {node} out:{out}")

    out = TREE_TO_OUTPUT_LIST(node.left, out)

    return out


def TEST__ARRAY_TO_TN_AS_ARGS(*args):
    args = list(args)
    # print("array to ll [0]", args)
    for idx,a in enumerate(args):
        # print(f"\t{idx}: {a} -- {type(a)}")
        if type(a) == type([]):
            args[idx] = GEN_TREE_FROM_LIST(a)
    # print("[1]", args)
    return args

def TEST__TN_TO_ARRAY_AS_ARGS(*args):
    args = list(args)
    # print("ll to array [0]", args)
    for idx,a in enumerate(args):
        # print(f"\t{idx}: {a} -- {type(a)}")
        if type(a) == TreeNode:
            args[idx] = TREE_TO_OUTPUT_LIST(a)
    # print("=> [1]", args)
    return args