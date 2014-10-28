sSET = 'SET'
sGET = 'GET'
sUNSET = 'UNSET'
sNUMEQUALTO = 'NUMEQUALTO'
sEND = 'END'
sNULL = 'NULL'

class SimpleDB(object):

    def __init__(self):
        # Mapping between CLI commands and methods
        self.COMMANDS = {
            sSET : self._set,
            sGET : self._get,
            sUNSET: self._unset,
            sNUMEQUALTO: self._num_equal_to,
            sEND : self._end
        }

        # current values stored
        self.CUR_DATA = {}

        # counts
        self.COUNTS = {}

    def parse_and_exec(self, line):
        '''
        Parse given line from CLI, and execute equivalent method.
        '''
        tokens = line.split(None, 1)
        command = tokens[0]
        args = tokens[1:]

        command = command.upper()

        # these commands have the name as first arg
        if command in [sSET, sGET, sUNSET]:

            # these commands specify a value after the name
            if len(args) > 0:
                args = args[0].split(None, 1)

                if command in [sSET]:
                    args[1] = int(args[1], 10)

        # these commands have the value as first arg
        elif command in [sNUMEQUALTO]:
            args[0] = int(args[0], 10)

        retVal = self._run_command(command, args)
        print line, '->', retVal
        return retVal

    def _run_command(self, command, args):
        '''
        Given the CLI text for the command and the parse argument list, run
        the corresponding method.
        '''
        func = self.COMMANDS[command]
        return func(*args)

    def _set(self, name, value):
        old_val = None
        if name in self.CUR_DATA:
            old_val = self.CUR_DATA[name]

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

    def _num_equal_to(self, value):
        if value in self.COUNTS:
            return self.COUNTS[value]

        return 0

    def _end(self):
        pass

if __name__ == '__main__':
    d = SimpleDB()

    # read input and exec commands
    import fileinput

    for line in fileinput.input():
        val = d.parse_and_exec(line)

        if val is not None:
            print str(val)

        if sEND in line:
            break
