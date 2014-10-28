from main import *

class TestSimpleDB(object):

    def setup(self):
        self.d = SimpleDB()

    def test_end(self):
        # for completeness...
        assert self.d.parse_and_exec('END') is None

    # -------------------------------------------------------------------------
    # Get/Set
    # -------------------------------------------------------------------------

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

        assert self.d.parse_and_exec('END') is None

    def test_set_and_get_multiple_values(self):
        assert self.d.parse_and_exec('GET ex') == sNULL
        assert self.d.parse_and_exec('GET ex2') == sNULL

        assert self.d.parse_and_exec('SET ex 10') is None
        assert self.d.parse_and_exec('GET ex') == 10

        assert self.d.parse_and_exec('SET ex2 20') is None
        assert self.d.parse_and_exec('GET ex2') == 20

        assert self.d.parse_and_exec('GET ex') == 10

        assert self.d.parse_and_exec('END') is None

    def test_set_and_unset_value(self):
        assert self.d.parse_and_exec('GET ex') == sNULL

        assert self.d.parse_and_exec('SET ex 10') is None
        assert self.d.parse_and_exec('GET ex') == 10

        assert self.d.parse_and_exec('UNSET ex') is None
        assert self.d.parse_and_exec('GET ex') == sNULL

    def test_set_and_unset_multiple_values(self):
        assert self.d.parse_and_exec('GET ex') == sNULL
        assert self.d.parse_and_exec('GET ex2') == sNULL

        assert self.d.parse_and_exec('SET ex 10') is None
        assert self.d.parse_and_exec('GET ex') == 10

        assert self.d.parse_and_exec('SET ex2 20') is None
        assert self.d.parse_and_exec('GET ex2') == 20
        assert self.d.parse_and_exec('GET ex') == 10

        assert self.d.parse_and_exec('UNSET ex') is None
        assert self.d.parse_and_exec('GET ex') == sNULL        
        assert self.d.parse_and_exec('GET ex2') == 20

        assert self.d.parse_and_exec('UNSET ex2') is None
        assert self.d.parse_and_exec('GET ex') == sNULL        
        assert self.d.parse_and_exec('GET ex2') == sNULL

        assert self.d.parse_and_exec('END') is None

    # -------------------------------------------------------------------------
    # num equal to
    # -------------------------------------------------------------------------

    def test_no_counts(self):
        assert self.d.parse_and_exec('NUMEQUALTO 10') == 0
        assert self.d.parse_and_exec('END') is None

    def test_simple_single_count(self):
        assert self.d.parse_and_exec('SET ex 10') is None
        assert self.d.parse_and_exec('GET ex') == 10

        assert self.d.parse_and_exec('NUMEQUALTO 10') == 1

        assert self.d.parse_and_exec('END') is None

    def test_simple_add_to_count(self):
        assert self.d.parse_and_exec('SET ex 10') is None
        assert self.d.parse_and_exec('GET ex') == 10

        assert self.d.parse_and_exec('NUMEQUALTO 10') == 1

        assert self.d.parse_and_exec('SET ex2 10') is None
        assert self.d.parse_and_exec('GET ex2') == 10

        assert self.d.parse_and_exec('NUMEQUALTO 10') == 2

        assert self.d.parse_and_exec('END') is None

    def test_set_and_set_again_with_counts(self):
        assert self.d.parse_and_exec('SET ex 10') is None
        assert self.d.parse_and_exec('GET ex') == 10

        assert self.d.parse_and_exec('NUMEQUALTO 10') == 1

        assert self.d.parse_and_exec('SET ex2 10') is None
        assert self.d.parse_and_exec('GET ex2') == 10

        assert self.d.parse_and_exec('NUMEQUALTO 10') == 2

        assert self.d.parse_and_exec('SET ex 20') is None
        assert self.d.parse_and_exec('GET ex') == 20
        assert self.d.parse_and_exec('GET ex2') == 10

        assert self.d.parse_and_exec('NUMEQUALTO 10') == 1
        assert self.d.parse_and_exec('NUMEQUALTO 20') == 1

        assert self.d.parse_and_exec('SET ex2 20') is None
        assert self.d.parse_and_exec('GET ex') == 20
        assert self.d.parse_and_exec('GET ex2') == 20

        assert self.d.parse_and_exec('NUMEQUALTO 10') == 0
        assert self.d.parse_and_exec('NUMEQUALTO 20') == 2

        assert self.d.parse_and_exec('END') is None

    def test_set_and_unset_with_counts(self):
        assert self.d.parse_and_exec('SET ex 10') is None
        assert self.d.parse_and_exec('GET ex') == 10

        assert self.d.parse_and_exec('NUMEQUALTO 10') == 1

        assert self.d.parse_and_exec('SET ex2 10') is None
        assert self.d.parse_and_exec('GET ex2') == 10

        assert self.d.parse_and_exec('NUMEQUALTO 10') == 2

        assert self.d.parse_and_exec('UNSET ex') is None
        assert self.d.parse_and_exec('GET ex') == sNULL        
        assert self.d.parse_and_exec('GET ex2') == 10

        assert self.d.parse_and_exec('NUMEQUALTO 10') == 1

        assert self.d.parse_and_exec('UNSET ex2') is None
        assert self.d.parse_and_exec('GET ex') == sNULL        
        assert self.d.parse_and_exec('GET ex2') == sNULL        

        assert self.d.parse_and_exec('NUMEQUALTO 10') == 0

        assert self.d.parse_and_exec('SET ex3 10') is None
        assert self.d.parse_and_exec('GET ex3') == 10
        assert self.d.parse_and_exec('GET ex') == sNULL        
        assert self.d.parse_and_exec('GET ex2') == sNULL  

        assert self.d.parse_and_exec('NUMEQUALTO 10') == 1

        assert self.d.parse_and_exec('END') is None

if __name__ == '__main__':
    import nose
    nose.main()
