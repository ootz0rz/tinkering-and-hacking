from main import *

class TestSimpleDB(object):

    def setup(self):
        self.d = SimpleDB()

    def test_set_and_get_single_value(self):
        '''
        SET ex 10
        GET ex
        END
        '''
        assert self.d.parse_and_exec('SET ex 10') is None
        assert self.d.parse_and_exec('GET ex') == 10
        assert self.d.parse_and_exec('END') is None

if __name__ == '__main__':
    import nose
    nose.main()
