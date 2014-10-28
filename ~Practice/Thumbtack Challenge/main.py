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

        Transactions currently store the reverse of any commands executed, so 
        that they may be literally rolled back. This might end up requiring a 
        lot of memory for larger transactions, as a lot of state information 
        is stored. 

        This means that commit operations are super fast as well, as nothing 
        needs to be done except removing the transaction state information 
        from memory.

        Thus, the only slow operation is ROLLBACK which runs in O(M) where M 
        is the number of commands executed within that transaction that modify
        any values.
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
        if self.is_in_transaction():
            if old_val is not None:
                self.TRANSACTION_STACKS[-1].append((sSET, [name, old_val]))
            else:
                self.TRANSACTION_STACKS[-1].append((sUNSET, [name]))

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
            if self.is_in_transaction():
                self.TRANSACTION_STACKS[-1].append((sSET, [name, cur_val]))

    def _num_equal_to(self, value):
        if value in self.COUNTS:
            return self.COUNTS[value]

        return 0

    def _end(self):
        pass

    def _begin(self):
        if not self.is_in_transaction():
            self.in_transaction = True

        self.TRANSACTION_STACKS.append([])

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
            while len(cur_stack) > 0:
                command, args = cur_stack.pop()
                self._run_cli_command(command, args)
            self.in_transaction = True

            if self.get_transaction_level() == 0:
                self.__reset_transactions()
        else:
            return sNO_TRANSACTION

    def __reset_transactions(self):
        self.in_transaction = False
        self.cur_transaction = -1

        # transactional stacks, each will hold a list of all the commands 
        # required to revert to a state before the transaction began
        #
        # Format:
        #   [(cmd, [arg1, arg2, ...]), (cmd2, [arg1, ...]), ...]
        self.TRANSACTION_STACKS = []

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
