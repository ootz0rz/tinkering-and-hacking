from listnode import ListNode
from typing import *

debug = False
class Solution:
    # O(nm)
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        global debug
        a = l1
        b = l2

        if debug: print(f'\n------\nmergeTwoLists l1<{l1}> l2<{l2}>')

        # choose head
        o = None
        if a is not None:
            if b is not None:
                if a.val > b.val:
                    o = b
                    b = b.next
                else:
                    o = a
                    a = a.next
            else:
                o = a
                a = a.next
        else:
            o = b
            b = b.next if b is not None else None

        first = o

        if debug: print(f'# a<{a}> b<{b}> == o<{o}> || first<{first}>')
        while (o is not None) and ((a is not None) or (b is not None)):
            if debug: print(f'\t -> a<{a}> b<{b}> == o<{o}> || first<{first}>')

            if a is None:
                if debug: print('\t\t -> a == null', end='')
                if b is None:           # a == null, b == null
                    if debug: print(' b == null')
                    break
                else:                   # a == null, b != null
                    if debug: print(' b != null')
                    o.next = b
                    b = b.next
            else:
                if debug: print('\t\t -> a != null', end='')
                if b is None:           # a != null, b == null
                    if debug: print(' b == null')
                    o.next = a
                    a = a.next
                else:                   # a != null, b != null
                    if debug: print(' b != null')
                    if a.val < b.val:
                        if debug: print(f'\t\t\t => a[{a.val}] < b[{b.val}]')
                        o.next = a
                        a = a.next
                    else:
                        if debug: print(f'\t\t\t => b[{b.val}] < a[{a.val}]')
                        o.next = b
                        b = b.next

            if o.next is not None:
                o = o.next

        return first


if __name__ == '__main__':
    debug = True
    s = Solution()

    lng = ListNode.genFromList

    # assert str(s.mergeTwoLists(lng([]), lng([]))) == str(lng([]))
    # assert str(s.mergeTwoLists(lng([0]), lng([]))) == str(lng([0]))
    # assert str(s.mergeTwoLists(lng([]), lng([0]))) == str(lng([0]))
    # assert str(s.mergeTwoLists(lng([0]), lng([0]))) == str(lng([0,0]))

    assert str(s.mergeTwoLists(lng([1,2,4]), lng([1,3,4]))) == str(lng([1,1,2,3,4,4]))
