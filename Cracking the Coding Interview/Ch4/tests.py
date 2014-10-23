from main import *

class test_q4_1(object):
    EMPTY = None
    SINGLE_NODE = TNode(0)
    SIMPLE_FULL = TNode(0, left=TNode(1), right=TNode(2))
    SIMPLE_UNBALANCED_LEFT_LINE = TNode(0, left=TNode(1, left=TNode(2)))

    def test_empty(self):
        assert q4_1(self.EMPTY) == True, "Empty tree"

    def test_single_node(self):
        assert q4_1(self.SINGLE_NODE) == True, "Single Node"

    def test_simple_full_tree(self):
        assert q4_1(self.SIMPLE_FULL) == True, "Simple full tree"

    def test_simple_unbalanced(self):
        assert q4_1(self.SIMPLE_UNBALANCED_LEFT_LINE) == False, "Simple unbalanced tree"

if __name__ == '__main__':
    import nose
    nose.main()
