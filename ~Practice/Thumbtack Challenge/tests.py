from main import *

class TestSimpleDB(object):

    def setup(self):
        self.d = SimpleDB()

    def test_get_non_existing_value(self):
        assert self.d.parse_and_exec('GET ex') == sNULL
        assert self.d.parse_and_exec('END') is None

    def test_set_and_get_single_value(self):
        assert self.d.parse_and_exec('SET ex 10') is None
        assert self.d.parse_and_exec('GET ex') == 10
        assert self.d.parse_and_exec('END') is None

    def test_set_value_twice(self):
        assert self.d.parse_and_exec('GET ex') == sNULL

        assert self.d.parse_and_exec('SET ex 10') is None
        assert self.d.parse_and_exec('GET ex') == 10

        assert self.d.parse_and_exec('SET ex 20') is None
        assert self.d.parse_and_exec('GET ex') == 20

    def test_set_and_get_multiple_values(self):
        assert self.d.parse_and_exec('GET ex') == sNULL

        assert self.d.parse_and_exec('SET ex 10') is None
        assert self.d.parse_and_exec('GET ex') == 10

        assert self.d.parse_and_exec('SET ex2 20') is None
        assert self.d.parse_and_exec('GET ex2') == 20

        assert self.d.parse_and_exec('GET ex') == 10

        assert self.d.parse_and_exec('END') is None

if __name__ == '__main__':
    import nose
    nose.main()
