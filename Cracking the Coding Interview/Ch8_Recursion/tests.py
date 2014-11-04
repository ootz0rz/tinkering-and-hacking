from main import *

class test_q4_1(object):

    def test_base_0(self):
        assert q4_1(0) == 0, 'Should be 0'

    def test_base_1(self):
        assert q4_1(1) == 1, 'Should be 1'

    def test_recursive_2(self):
        assert q4_1(2) == 1, 'Should be 1'

    def test_recursive_5(self):
        assert q4_1(5) == 5, 'Should be 5'

    def test_recursive_10(self):
        assert q4_1(10) == 55, 'Should be 55'

class test_q4_3(object):

    def _validateAssert(self, r1, a1):
        sets_r1 = frozenset([frozenset(c) for c in r1])
        sets_a1 = frozenset([frozenset(c) for c in a1])

        for r in sets_r1:
            assert r in sets_a1, "Extra element <%s> in returned answer" % str(list(r))

        for a in sets_a1:
            assert a in sets_r1, "Missing element <%s> in returned answer" % str(list(a))

    def test_empty(self):
        self._validateAssert(
            q4_3([]),
            [[]]
        )

    def test_single(self):
        self._validateAssert(
            q4_3([1]),
            [[], [1]]
        )

    def test_small(self):
        self._validateAssert(
            q4_3([1, 2]),
            [[], [1], [2], [1, 2]]
        )

    def test_large(self):
        self._validateAssert(
            q4_3([1, 2, 3]),
            [
                [], [1], [2], [3],
                [1, 2], [1, 3], [2, 3],
                [1, 2, 3]
            ]
        )

class test_q4_4(object):

    def _validateAssert(self, r1, a1):
        print 'func result:', r1
        print 'expected   :', a1

        for r in r1:
            assert r in a1, "Extra element <%s> in returned answer" % str(r)

        for a in a1:
           assert a in r1, "Missing element <%s> in returned answer" % str(a)

    def test_empty(self):
        self._validateAssert(
            q4_4(''),
            ['']
        )

    def test_single(self):
        self._validateAssert(
            q4_4('a'),
            [
                'a'
            ]
        )

    def test_small(self):
        self._validateAssert(
            q4_4('ab'),
            [
                'ab', 'ba'
            ]
        )

    def test_large(self):
        self._validateAssert(
            q4_4('abc'),
            [
                'abc', 'acb', 'bac',
                'bca', 'cab', 'cba'
            ]
        )

class test_q4_5(object):

    def _validateAssert(self, r1, a1):
        print 'func result:', r1
        print 'expected   :', a1

        for r in r1:
            assert r in a1, "Extra element <%s> in returned answer" % str(r)

        for a in a1:
           assert a in r1, "Missing element <%s> in returned answer" % str(a)

    def test_empty(self):
        self._validateAssert(
            q4_5(0),
            ['']
        )

    def test_single(self):
        self._validateAssert(
            q4_5(1),
            [
                '()'
            ]
        )

    def test_small(self):
        self._validateAssert(
            q4_5(2),
            [
                '(())', '()()'
            ]
        )

    def test_large(self):
        self._validateAssert(
            q4_5(3),
            [
                '()()()', '(())()', '(()())',
                '()(())', '((()))'
            ]
        )

if __name__ == '__main__':
    import nose
    nose.main()
