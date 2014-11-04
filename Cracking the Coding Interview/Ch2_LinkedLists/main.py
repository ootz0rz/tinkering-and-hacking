class Node(object):
    '''
    Helper class for questions below.
    '''
    n = None
    data = None

    def __init__(self, d=None):
        self.data = d

    def append(self, d):
        end = Node(d)
        n = self

        while n.n is not None:
            n = n.n

        n.n = end

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        n = self
        l = [n.data]

        while n.n is not None:
            n = n.n
            l.append(n.data)

        return str(l)

def q2_2():
    '''
    Basically keep two cursors. One is used to move to the end, the second will
    lag n spaces behind to give you the nth to last element within the list.
    '''
    pass

def q2_3(n):
    '''
    Given a node somewhere within a linked list, delete it but keep the LL
    continuous.
    '''

    # idea: copy next node to current node, delete next node
    pass

def q2_4(n1, n2):
    '''
    Given two numbers stored as linked lists in reverse order such that the
    head contains the 1s digit, add the two numbers and return the sum as a
    linked list.
    '''
    _n1 = n1
    _n2 = n2

    rollover = 0
    out = Node()
    cur_node = out
    while True:
        left = 0
        right = 0

        # get values to add
        if n1 is not None:
            left = n1.data
        if n2 is not None:
            right = n2.data

        # add
        total = left + right + rollover
        cur_val = total % 10
        rollover = 1 if total >= 10 else 0

        # store in output
        cur_node.data = cur_val

        # update pointers
        if n1 is not None: n1 = n1.n
        if n2 is not None: n2 = n2.n

        # if both n1 and n2 are None, and nothing to roll over, 
        # then we've finished
        if (n1 is None) and (n2 is None) and rollover == 0:
            break

        # otherwise, lets add another node and continue
        cur_node.n = Node()
        cur_node = cur_node.n

    print _n1, '+', _n2, '=', out
    return out

def q2_5(head):
    '''
    Given a circular linked list, implement an algorithm which returns node at 
    the beginning of the loop.
    '''

    '''
    Basically, same as finding a cycle within a linked list. Have two pointers,
    one moving at a pace of +1 nodes per cycle, another at +2 (twice as fast).

    If the cycle is at the start, they will again meet at the start of the
    loop. If we start n nodes away from the start of the cycle, they will
    meet n nodes from the start of the cycle (but still within it). 

    Once they meet, advance one of the pointers another n spots and that will
    be the start of the cycle.
    '''
    pass