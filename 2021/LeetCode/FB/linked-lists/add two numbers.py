from listnode import ListNode
from typing import *

debug = False
class Solution:
    # O(nm)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        global debug
        a = l1
        b = l2

        o = ListNode()
        first = o
        carry = 0
        while (a is not None) or (b is not None):
            val = 0

            # add values
            if a is not None:
                val = val + a.val
                a = a.next

            if b is not None:
                val = val + b.val
                b = b.next

            # add carry
            val = val + carry

            # calc final vals to save
            carry = val // 10
            val = val % 10

            o.val = val

            if (a is not None) or (b is not None):
                o.next = ListNode()
                o = o.next

        if carry > 0:
            o.next = ListNode(carry)

        if debug: print(f'l1<{l1}> l2<{l2}> == res<{first}>')
        return first


if __name__ == '__main__':
    debug = True
    s = Solution()

    lng = ListNode.genFromList

    assert str(s.addTwoNumbers(lng([0]), lng([0]))) == str(lng([0]))
    assert str(s.addTwoNumbers(lng([2,4,3]), lng([5,6,4]))) == str(lng([7,0,8]))
    assert str(s.addTwoNumbers(lng([9,9,9,9,9,9,9]), lng([9,9,9,9]))) == str(lng([8,9,9,9,0,0,0,1]))
