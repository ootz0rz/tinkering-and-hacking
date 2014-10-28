sSET = 'SET'
sGET = 'GET'
sUNSET = 'UNSET'
sNUMEQUALTO = 'NUMEQUALTO'
sEND = 'END'
sNULL = 'NULL'

sBEGIN = 'BEGIN'
sROLLBACK = 'ROLLBACK'
sCOMMIT = 'COMMIT'
sNO_TRANSACTION = 'NO TRANSACTION'

class SimpleDB(object):
    '''
    A simple database that allows for storage and retrieval of data, and basic
    transactional commits, designed to be used from a command line interface.

    Some notes on design decisions:
        I made the GET/SET/UNSET/NUMEQUALTO methods as fast as possible, all 
        run in O(1) respective to number of total variables in the database. 
        This is because there is only ever a single state for the database
        stored as two dictionaries: one for the name/value pairs, and another 
        for the counts of values. These are updated as operations are executed.
        This means, to keep NUMEQUALTO fast, additional memory is required for
        its corresponding dictionary as well.

        Since it's noted that transactions will only modify a small number of
        individual variables, but can then potentially have many different
        commands per transaction, each transaction keeps track of what the
        database state looked like before the transactions current state. This
        allows us to only have to store at most 1 state item per variable in
        the database, per transaction. i.e. using at most O(N) storage per
        transaction, where N is the number of variables modified during the 
        transaction.

        This means that commit operations are super fast as well, as nothing 
        needs to be done except removing the transaction state information 
        from memory.

        Thus, the only slow operation, computationally, is ROLLBACK which runs
        in O(N) where N is the number of variables modified during the 
        transaction. It also updates the dictionary for NUMEQUALTO to reflect
        the current state after a rollback. It would have been possible to
        store this data within the transaction state as well, but that would
        require more memory, where as there were no restrictions on run time
        for ROLLBACK.
    '''

    def __init__(self):
        # Mapping between CLI commands and methods
        self.COMMANDS = {
            sSET : self._set,
            sGET : self._get,
            sUNSET: self._unset,
            sNUMEQUALTO: self._num_equal_to,
            sEND : self._end,

            sBEGIN : self._begin,
            sCOMMIT : self._commit,
            sROLLBACK : self._rollback
        }

        # current values stored
        self.CUR_DATA = {}

        # counts
        self.COUNTS = {}

        self.__reset_transactions()

    def is_in_transaction(self):
        return self.in_transaction

    def get_transaction_level(self):
        return len(self.TRANSACTION_STACKS)

    def parse_and_exec(self, line, print_debug=False):
        '''
        Parse given line from CLI, and execute equivalent method.
        '''
        tokens = line.split()
        command = tokens[0]
        args = tokens[1:]

        command = command.upper()

        # these commands have the name as first arg
        if command in [sSET, sGET, sUNSET]:

            # these commands specify a value after the name
            if command in [sSET]:
                if len(args) > 0:
                    args[1] = int(args[1], 10)

        # these commands have the value as first arg
        elif command in [sNUMEQUALTO]:
            args[0] = int(args[0], 10)

        retVal = self._run_cli_command(command, args)

        if print_debug:
            print line, '->', retVal

        return retVal

    def _run_cli_command(self, command, args):
        '''
        Given the CLI text for the command and the parse argument list, run
        the corresponding method.
        '''
        func = self.COMMANDS[command]
        return func(*args)

    def _get_cur_stack(self):
        return self.TRANSACTION_STACKS[-1]

    def _set(self, name, value):
        # retain old value for count update
        old_val = None
        if name in self.CUR_DATA:
            old_val = self.CUR_DATA[name]

        # set new val
        self.CUR_DATA[name] = value

        # update counts
        if not (value in self.COUNTS):
            self.COUNTS[value] = 0
        self.COUNTS[value] += 1

        if old_val is not None:
            if self.COUNTS[old_val] == 1:
                del self.COUNTS[old_val]
            else:
                self.COUNTS[old_val] -= 1

        # update transaction state if necessary
        if self.is_in_transaction() and not (name in self._get_cur_stack()):
            if old_val is not None:
                self._get_cur_stack()[name] = old_val
            else:
                self._get_cur_stack()[name] = None

    def _get(self, name):
        if not (name in self.CUR_DATA):
            return sNULL

        return self.CUR_DATA[name]

    def _unset(self, name):
        if name in self.CUR_DATA:
            cur_val = self.CUR_DATA[name]

            del self.CUR_DATA[name]

            # update count
            if cur_val in self.COUNTS:
                self.COUNTS[cur_val] -= 1
            else:
                del self.COUNTS[cur_val]

            # update transaction state if necessary
            if self.is_in_transaction() and not (name in self._get_cur_stack()):
                self._get_cur_stack()[name] = cur_val

    def _num_equal_to(self, value):
        if value in self.COUNTS:
            return self.COUNTS[value]

        return 0

    def _end(self):
        pass

    def _begin(self):
        if not self.is_in_transaction():
            self.in_transaction = True

        self.TRANSACTION_STACKS.append({})

    def _commit(self):
        if self.is_in_transaction():
            self.__reset_transactions()
        else:
            return sNO_TRANSACTION

    def _rollback(self):
        if self.is_in_transaction():
            # roll back the most recent transaction only
            cur_stack = self.TRANSACTION_STACKS.pop()

            self.in_transaction = False
            for name, value in cur_stack.items():
                if value is None:
                    self._unset(name)
                else:
                    self._set(name, value)
            self.in_transaction = True

            if self.get_transaction_level() == 0:
                self.__reset_transactions()

            self.__update_num_equal_to()
        else:
            return sNO_TRANSACTION

    def __reset_transactions(self):
        self.in_transaction = False
        self.cur_transaction = -1

        # transactional stacks, each will hold the state of the variables
        # touched during the transaction as they were before the stack was 
        # created.
        #
        # Format:
        # {
        #     'name': previous value/None,
        #     'name2': previous value/None,
        #     ...
        # }
        #
        # Where a value of None would mean this variable did not exist before
        self.TRANSACTION_STACKS = []

    def __update_num_equal_to(self):
        '''
        Re-calculate the number of occurances per each value in our database.
        '''
        self.COUNTS = {}

        for name, value in self.CUR_DATA.items():
            if not (value in self.COUNTS):
                self.COUNTS[value] = 0
            self.COUNTS[value] += 1

if __name__ == '__main__':
    d = SimpleDB()

    # read from stdin/file and exec commands
    import fileinput

    for line in fileinput.input():
        val = d.parse_and_exec(line)

        if val is not None:
            print str(val)

        if sEND in line:
            break
