from main import *

class TestSimpleDB(object):

    def setup(self):
        self.d = SimpleDB()

        self.parse = lambda line: self.d.parse_and_exec(line, print_debug=True)

    def test_end(self):
        # for completeness...
        assert self.parse('END') is None

    # -------------------------------------------------------------------------
    # Get/Set
    # -------------------------------------------------------------------------

    def test_get_non_existing_value(self):
        assert self.parse('GET ex') == sNULL
        assert self.parse('END') is None

    def test_set_and_get_single_value(self):
        assert self.parse('SET ex 10') is None
        assert self.parse('GET ex') == 10
        assert self.parse('END') is None

    def test_set_value_twice(self):
        assert self.parse('GET ex') == sNULL

        assert self.parse('SET ex 10') is None
        assert self.parse('GET ex') == 10

        assert self.parse('SET ex 20') is None
        assert self.parse('GET ex') == 20

        assert self.parse('END') is None

    def test_set_and_get_multiple_values(self):
        assert self.parse('GET ex') == sNULL
        assert self.parse('GET ex2') == sNULL

        assert self.parse('SET ex 10') is None
        assert self.parse('GET ex') == 10

        assert self.parse('SET ex2 20') is None
        assert self.parse('GET ex2') == 20

        assert self.parse('GET ex') == 10

        assert self.parse('END') is None

    def test_set_and_unset_value(self):
        assert self.parse('GET ex') == sNULL

        assert self.parse('SET ex 10') is None
        assert self.parse('GET ex') == 10

        assert self.parse('UNSET ex') is None
        assert self.parse('GET ex') == sNULL

        assert self.parse('END') is None

    def test_set_and_unset_multiple_values(self):
        assert self.parse('GET ex') == sNULL
        assert self.parse('GET ex2') == sNULL

        assert self.parse('SET ex 10') is None
        assert self.parse('GET ex') == 10

        assert self.parse('SET ex2 20') is None
        assert self.parse('GET ex2') == 20
        assert self.parse('GET ex') == 10

        assert self.parse('UNSET ex') is None
        assert self.parse('GET ex') == sNULL        
        assert self.parse('GET ex2') == 20

        assert self.parse('UNSET ex2') is None
        assert self.parse('GET ex') == sNULL        
        assert self.parse('GET ex2') == sNULL

        assert self.parse('END') is None

    # -------------------------------------------------------------------------
    # num equal to
    # -------------------------------------------------------------------------

    def test_no_counts(self):
        assert self.parse('NUMEQUALTO 10') == 0
        assert self.parse('END') is None

    def test_simple_single_count(self):
        assert self.parse('SET ex 10') is None
        assert self.parse('GET ex') == 10

        assert self.parse('NUMEQUALTO 10') == 1

        assert self.parse('END') is None

    def test_simple_add_to_count(self):
        assert self.parse('SET ex 10') is None
        assert self.parse('GET ex') == 10

        assert self.parse('NUMEQUALTO 10') == 1

        assert self.parse('SET ex2 10') is None
        assert self.parse('GET ex2') == 10

        assert self.parse('NUMEQUALTO 10') == 2

        assert self.parse('END') is None

    def test_set_and_set_again_with_counts(self):
        assert self.parse('SET ex 10') is None
        assert self.parse('GET ex') == 10

        assert self.parse('NUMEQUALTO 10') == 1

        assert self.parse('SET ex2 10') is None
        assert self.parse('GET ex2') == 10

        assert self.parse('NUMEQUALTO 10') == 2

        assert self.parse('SET ex 20') is None
        assert self.parse('GET ex') == 20
        assert self.parse('GET ex2') == 10

        assert self.parse('NUMEQUALTO 10') == 1
        assert self.parse('NUMEQUALTO 20') == 1

        assert self.parse('SET ex2 20') is None
        assert self.parse('GET ex') == 20
        assert self.parse('GET ex2') == 20

        assert self.parse('NUMEQUALTO 10') == 0
        assert self.parse('NUMEQUALTO 20') == 2

        assert self.parse('END') is None

    def test_set_and_unset_with_counts(self):
        assert self.parse('SET ex 10') is None
        assert self.parse('GET ex') == 10

        assert self.parse('NUMEQUALTO 10') == 1

        assert self.parse('SET ex2 10') is None
        assert self.parse('GET ex2') == 10

        assert self.parse('NUMEQUALTO 10') == 2

        assert self.parse('UNSET ex') is None
        assert self.parse('GET ex') == sNULL        
        assert self.parse('GET ex2') == 10

        assert self.parse('NUMEQUALTO 10') == 1

        assert self.parse('UNSET ex2') is None
        assert self.parse('GET ex') == sNULL        
        assert self.parse('GET ex2') == sNULL        

        assert self.parse('NUMEQUALTO 10') == 0

        assert self.parse('SET ex3 10') is None
        assert self.parse('GET ex3') == 10
        assert self.parse('GET ex') == sNULL        
        assert self.parse('GET ex2') == sNULL  

        assert self.parse('NUMEQUALTO 10') == 1

        assert self.parse('END') is None

    # -------------------------------------------------------------------------
    # transactions
    # -------------------------------------------------------------------------

    def test_default_no_transaction(self):
        assert not self.d.is_in_transaction() 
        assert self.d.get_transaction_level() == 0

    def test_default_commit_null_transaction(self):
        assert self.parse('COMMIT') == sNO_TRANSACTION

    def test_default_rollback_null_transaction(self):
        assert self.parse('ROLLBACK') == sNO_TRANSACTION

    def test_start_transaction(self):
        assert self.parse('BEGIN') is None
        assert self.d.is_in_transaction()
        assert self.d.get_transaction_level() == 1

        assert self.parse('END') is None

    def test_simple_start_and_commit_empty_transaction(self):
        assert self.parse('BEGIN') is None
        assert self.d.is_in_transaction()
        assert self.d.get_transaction_level() == 1

        assert self.parse('COMMIT') is None
        assert not self.d.is_in_transaction() 
        assert self.d.get_transaction_level() == 0

        assert self.parse('ROLLBACK') == sNO_TRANSACTION
        assert self.parse('COMMIT') == sNO_TRANSACTION

        assert self.parse('END') is None

    def test_simple_start_and_commit_changes_transaction(self):
        assert self.parse('SET ex 10') is None
        assert self.parse('GET ex') == 10
        assert self.parse('NUMEQUALTO 10') == 1
        assert self.parse('NUMEQUALTO 20') == 0

        assert self.parse('BEGIN') is None
        assert self.d.is_in_transaction()
        assert self.d.get_transaction_level() == 1

        assert self.parse('SET ex 20') is None
        assert self.parse('GET ex') == 20
        assert self.parse('NUMEQUALTO 10') == 0
        assert self.parse('NUMEQUALTO 20') == 1

        assert self.parse('COMMIT') is None
        assert not self.d.is_in_transaction() 
        assert self.d.get_transaction_level() == 0
        assert self.parse('GET ex') == 20
        assert self.parse('NUMEQUALTO 10') == 0
        assert self.parse('NUMEQUALTO 20') == 1

        assert self.parse('END') is None

    def test_simple_start_and_rollback_set_changes_transaction(self):
        assert self.parse('SET ex 10') is None
        assert self.parse('GET ex') == 10
        assert self.parse('NUMEQUALTO 10') == 1
        assert self.parse('NUMEQUALTO 20') == 0

        assert self.parse('BEGIN') is None
        assert self.d.is_in_transaction()
        assert self.d.get_transaction_level() == 1

        assert self.parse('SET ex 20') is None
        assert self.parse('GET ex') == 20
        assert self.parse('NUMEQUALTO 10') == 0
        assert self.parse('NUMEQUALTO 20') == 1

        assert self.parse('ROLLBACK') is None
        assert not self.d.is_in_transaction() 
        assert self.d.get_transaction_level() == 0
        assert self.parse('GET ex') == 10
        assert self.parse('NUMEQUALTO 10') == 1
        assert self.parse('NUMEQUALTO 20') == 0

        assert self.parse('END') is None

    def test_start_and_rollback_set_changes_transaction(self):
        assert self.parse('NUMEQUALTO 10') == 0
        assert self.parse('NUMEQUALTO 20') == 0

        assert self.parse('BEGIN') is None
        assert self.d.is_in_transaction()
        assert self.d.get_transaction_level() == 1

        assert self.parse('SET ex 10') is None
        assert self.parse('GET ex') == 10
        assert self.parse('NUMEQUALTO 10') == 1
        assert self.parse('NUMEQUALTO 20') == 0

        assert self.parse('BEGIN') is None
        assert self.d.is_in_transaction()
        assert self.d.get_transaction_level() == 2

        assert self.parse('SET ex 20') is None
        assert self.parse('GET ex') == 20
        assert self.parse('NUMEQUALTO 10') == 0
        assert self.parse('NUMEQUALTO 20') == 1

        assert self.parse('ROLLBACK') is None
        assert self.d.is_in_transaction() 
        assert self.d.get_transaction_level() == 1
        assert self.parse('GET ex') == 10
        assert self.parse('NUMEQUALTO 10') == 1
        assert self.parse('NUMEQUALTO 20') == 0

        assert self.parse('ROLLBACK') is None
        assert not self.d.is_in_transaction() 
        assert self.d.get_transaction_level() == 0
        assert self.parse('GET ex') == sNULL
        assert self.parse('NUMEQUALTO 10') == 0
        assert self.parse('NUMEQUALTO 20') == 0

        assert self.parse('END') is None

    def test_start_and_rollback_unset_changes_transaction(self):
        assert self.parse('SET ex 10') is None
        assert self.parse('GET ex') == 10
        assert self.parse('NUMEQUALTO 10') == 1
        assert self.parse('NUMEQUALTO 20') == 0

        assert self.parse('BEGIN') is None
        assert self.d.is_in_transaction()
        assert self.d.get_transaction_level() == 1

        assert self.parse('SET ex 20') is None
        assert self.parse('GET ex') == 20
        assert self.parse('NUMEQUALTO 10') == 0
        assert self.parse('NUMEQUALTO 20') == 1

        assert self.parse('UNSET ex') is None
        assert self.parse('GET ex') == sNULL
        assert self.parse('NUMEQUALTO 10') == 0
        assert self.parse('NUMEQUALTO 20') == 0

        assert self.parse('ROLLBACK') is None
        assert not self.d.is_in_transaction() 
        assert self.d.get_transaction_level() == 0
        assert self.parse('GET ex') == 10
        assert self.parse('NUMEQUALTO 10') == 1
        assert self.parse('NUMEQUALTO 20') == 0

        assert self.parse('END') is None

    def test_rollback_after_commit_transaction(self):
        assert self.parse('BEGIN') is None
        assert self.d.is_in_transaction()
        assert self.d.get_transaction_level() == 1

        assert self.parse('SET ex 30') is None
        assert self.parse('GET ex') == 30
        assert self.parse('NUMEQUALTO 30') == 1
        assert self.parse('NUMEQUALTO 40') == 0

        assert self.parse('BEGIN') is None
        assert self.d.is_in_transaction()
        assert self.d.get_transaction_level() == 2

        assert self.parse('SET ex 40') is None
        assert self.parse('GET ex') == 40
        assert self.parse('NUMEQUALTO 30') == 0
        assert self.parse('NUMEQUALTO 40') == 1

        assert self.parse('COMMIT') is None
        assert not self.d.is_in_transaction() 
        assert self.d.get_transaction_level() == 0

        assert self.parse('GET ex') == 40
        assert self.parse('NUMEQUALTO 30') == 0
        assert self.parse('NUMEQUALTO 40') == 1

        assert self.parse('ROLLBACK') == sNO_TRANSACTION

        assert self.parse('GET ex') == 40
        assert self.parse('NUMEQUALTO 30') == 0
        assert self.parse('NUMEQUALTO 40') == 1

        assert self.parse('END') is None

    def test_start_and_rollback_once_and_commit_changes_transaction(self):
        assert self.parse('NUMEQUALTO 10') == 0
        assert self.parse('NUMEQUALTO 20') == 0

        assert self.parse('BEGIN') is None
        assert self.d.is_in_transaction()
        assert self.d.get_transaction_level() == 1

        assert self.parse('SET ex 10') is None
        assert self.parse('GET ex') == 10
        assert self.parse('NUMEQUALTO 10') == 1
        assert self.parse('NUMEQUALTO 20') == 0

        assert self.parse('BEGIN') is None
        assert self.d.is_in_transaction()
        assert self.d.get_transaction_level() == 2

        assert self.parse('SET ex 20') is None
        assert self.parse('GET ex') == 20
        assert self.parse('NUMEQUALTO 10') == 0
        assert self.parse('NUMEQUALTO 20') == 1

        assert self.parse('ROLLBACK') is None
        assert self.d.is_in_transaction() 
        assert self.d.get_transaction_level() == 1
        assert self.parse('GET ex') == 10
        assert self.parse('NUMEQUALTO 10') == 1
        assert self.parse('NUMEQUALTO 20') == 0

        assert self.parse('COMMIT') is None
        assert not self.d.is_in_transaction() 
        assert self.d.get_transaction_level() == 0
        assert self.parse('GET ex') == 10
        assert self.parse('NUMEQUALTO 10') == 1
        assert self.parse('NUMEQUALTO 20') == 0

        assert self.parse('END') is None

    def test_start_and_rollback_multiple_variables_transaction(self):
        assert self.parse('NUMEQUALTO 10') == 0

        assert self.parse('SET a 10') is None
        assert self.parse('GET a') == 10
        assert self.parse('NUMEQUALTO 10') == 1

        assert self.parse('BEGIN') is None
        assert self.d.is_in_transaction()
        assert self.d.get_transaction_level() == 1
        assert self.parse('SET b 10') is None
        assert self.parse('GET b') == 10
        assert self.parse('NUMEQUALTO 10') == 2

        assert self.parse('BEGIN') is None
        assert self.d.is_in_transaction()
        assert self.d.get_transaction_level() == 2
        assert self.parse('SET c 10') is None
        assert self.parse('GET c') == 10
        assert self.parse('NUMEQUALTO 10') == 3

        assert self.parse('ROLLBACK') is None
        assert self.d.is_in_transaction()
        assert self.d.get_transaction_level() == 1
        assert self.parse('GET a') == 10
        assert self.parse('GET b') == 10
        assert self.parse('GET c') == sNULL
        assert self.parse('NUMEQUALTO 10') == 2

        assert self.parse('ROLLBACK') is None
        assert not self.d.is_in_transaction()
        assert self.d.get_transaction_level() == 0
        assert self.parse('GET a') == 10
        assert self.parse('GET b') == sNULL
        assert self.parse('GET c') == sNULL
        assert self.parse('NUMEQUALTO 10') == 1

        assert self.parse('END') is None

if __name__ == '__main__':
    import nose
    nose.main()
