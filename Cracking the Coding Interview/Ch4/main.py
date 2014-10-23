class TNode(object):
    '''
    Helper class for binary tree nodes.
    '''

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.L = left
        self.R = right


def q4_1(root):
    '''
    True iff tree at node root is balanced.

    i.e. no two leaf nodes differ in distance from the root by more than one.
    '''

    def _height(node, compare_func=min):
        if node is not None:
            return 1 + compare_func(
                _height(node.L, compare_func),
                _height(node.R, compare_func))

        return 0

    # find min and max heights for each leaf in the tree
    _min = _height(root, min)
    _max = _height(root, max)

    # check difference between the two
    return (_max - _min) <= 1