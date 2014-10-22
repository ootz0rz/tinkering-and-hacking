from main import *

class test_q1_1(object):

    def test_empty(self):
        assert q1_1('') == True, "Empty string, vacuously True"

    def test_basic(self):
        assert q1_1('a') == True, "Single unique character"

    def test_larger_string(self):
        assert q1_1('abc') == True, "Unique characters"

    def test_repeat_double(self):
        assert q1_1('aa') == False, "Two of the same character"

    def test_repeat_double_and_more(self):
        assert q1_1('aba') == False, "Two of the same character"

    def test_repeat_double_and_more_2(self):
        assert q1_1('baac') == False, "Two of the same character"

    def test_repeat_multiple_repeated(self):
        assert q1_1('babcdefba') == False, "Multiple sets of repeated characters"

TERM = '\0'
class test_q1_2(object):

    def test_empty(self):
        assert q1_2([''], TERM) == [''], "Empty input"

    def test_base(self):
        assert q1_2([TERM], TERM) == [TERM], "Empty string"

    def test_single(self):
        assert q1_2(['a', TERM], TERM) == ['a', TERM], "Single character"

    def test_simple(self):
        assert q1_2(['a', 'b', TERM], TERM) == ['b', 'a', TERM], "Simple, short string"

    def test_longer_even_length(self):
        assert q1_2(['a', 'b', 'c', 'd', TERM], TERM) == ['d', 'c', 'b', 'a', TERM], "Longer even length string"

    def test_longer_odd_length(self):
        assert q1_2(['a', 'b', 'c', 'd', 'e', TERM], TERM) == ['e', 'd', 'c', 'b', 'a', TERM], "Longer odd length string"

if __name__ == '__main__':
    import nose
    nose.main()
