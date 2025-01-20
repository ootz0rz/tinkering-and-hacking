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
        return f"V: {self.val} L: {self.left if self.left is None else self.left.__all__()} R: {self.right if self.right is None else self.right.__all__()}"
