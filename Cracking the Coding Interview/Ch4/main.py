class TNode(object):

    '''
    Helper class for binary tree nodes.
    '''

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.L = left
        self.R = right

    def __eq__(self, o):
        return \
            self.data == o.data \
            and self.L == o.L \
            and self.R == o.R

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "<TNode:%s,L=%s,R=%s>" % (self.data, self.L, self.R, )


    def p(self, indent=0):
        '''
        Print a pretty representation of the tree rooted at this node.
        '''
        if self.R is not None:
            self.R.p(indent + 1)
        else:
            print '\t' * (indent + 1), "None"
            
        print '\t' * indent, self.data

        if self.L is not None:
            self.L.p(indent + 1)
        else:
            print '\t' * (indent + 1), "None"


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


def q4_2(graph, n1, n2):
    '''
    Given a directed graph, return True iff there is a path between n1 and n2.
    '''

    # Idea: start at n1, do a brute force search for n2

    # Could also use something like dijkstra's or A* or w/e for perf later


def q4_3(arr):
    '''
    Create a balanced binary tree with from the values in the given array, arr.

    Assumes arr is sorted.
    '''
    if arr is None or len(arr) == 0:
        return None

    # Take the middle element as current node, then add all the items to the
    # left recursively, and likewise to the right
    mid = len(arr) / 2
    mid_val = arr[mid]
    left_arr = arr[:mid]
    right_arr = arr[mid + 1:]

    node = TNode(data=mid_val,
                 left=q4_3(left_arr),
                 right=q4_3(right_arr))

    return node
