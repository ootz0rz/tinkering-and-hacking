from __future__ import annotations
from typing import Optional, Type, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: Optional[int] = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

    def GEN_FROM_LIST(l: List[int]) -> ListNode:
        print("GEN_FROM_LIST -- ", l)
        if len(l) == 0:
            return None

        head = ListNode(l[0])

        ptr = head
        print("\tHead: ", head)
        for e in l[1:]:
            node = ListNode(e)
            ptr.next = node
            ptr = ptr.next
            print("\tNext Node: ", e)

        print("-> Return Head: ", head)
        return head

    def __repr__(self):
        return f"{self.val}, next: {self.next}"

    def __str__(self):
        return str(self.to_list())  # ", ".join(s)

    def to_list(self):
        ptr = self

        s = []
        while ptr is not None:
            s.append(ptr.val)
            ptr = ptr.next

        return s


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(-999, head)

        ptr = start

        while head is not None:
            if (head.next is not None) and (head.val == head.next.val):
                # skip ahead
                while (head.next is not None) and (head.val == head.next.val):
                    head = head.next

                # set the mark
                ptr.next = head.next
            else:
                ptr = ptr.next

            head = head.next

        return start.next


if __name__ == "__main__":

    h = ListNode.GEN_FROM_LIST([5, 10, 15])
    print(h)

    s = Solution()

    h1 = ListNode.GEN_FROM_LIST([1, 2, 3, 3, 4, 4, 5])
    print(s.deleteDuplicates(h1))
