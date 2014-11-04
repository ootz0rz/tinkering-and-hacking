from main import *

EMPTY = None
SINGLE_NODE = TNode(0)
SIMPLE_FULL = TNode(1, left=TNode(0), right=TNode(2))
SIMPLE_UNEVEN = TNode(2, left=TNode(1, left=TNode(0)), right=TNode(3))
SIMPLE_UNBALANCED_LEFT_LINE = TNode(0, left=TNode(1, left=TNode(2)))

class test_q4_1(object):
    def test_empty(self):
        assert q4_1(EMPTY) == True, "Empty tree"

    def test_single_node(self):
        assert q4_1(SINGLE_NODE) == True, "Single Node"

    def test_simple_full_tree(self):
        assert q4_1(SIMPLE_FULL) == True, "Simple full tree"

    def test_simple_unbalanced(self):
        assert q4_1(SIMPLE_UNBALANCED_LEFT_LINE) == False, "Simple unbalanced tree"

class test_q4_3(object):

    def test_empty(self):
        assert q4_3([]) == EMPTY, "Empty list"

    def test_single_node(self):
        assert q4_3([0]) == SINGLE_NODE, "Single Node"

    def test_simple_full_tree(self):
        assert q4_3([0, 1, 2]) == SIMPLE_FULL, "Simple full tree"

    def test_simple_uneven_tree(self):
        assert q4_3([0, 1, 2, 3]) == SIMPLE_UNEVEN, "Simple uneven tree"

if __name__ == '__main__':
    import nose
    nose.main()
