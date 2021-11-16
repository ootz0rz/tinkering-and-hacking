from listnode import Node
from typing import *

debug = False
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        global debug

        if head is None:
            if debug: print(f'head<{head}> == first<{None}>')
            return None

        oldnode_to_newnode = {} # oldnode -> newnode

        o = Node(head.val)
        first = o
        oldnode_to_newnode[head] = o

        pointer = head
        while pointer is not None:
            target_value = pointer.val
            target_random = pointer.random

            node_random = None
            if not (target_random is None):
                if not (target_random in oldnode_to_newnode):
                    node_random = oldnode_to_newnode[target_random] = Node(target_random.val)
                else:
                    node_random = oldnode_to_newnode[target_random]

            curr = None
            if not (pointer in oldnode_to_newnode):
                curr = oldnode_to_newnode[pointer] = Node(target_value)
            else:
                curr = oldnode_to_newnode[pointer]

            node_next = None
            if pointer.next is not None:
                if not (pointer.next in oldnode_to_newnode):
                    oldnode_to_newnode[pointer.next] = node_next = Node(pointer.next.val)
                else:
                    node_next = oldnode_to_newnode[pointer.next]

            curr.next = node_next
            curr.random = node_random

            pointer = pointer.next


        return first


if __name__ == '__main__':
    debug = True
    s = Solution()

    lng = Node.genFromList

    # print('test')
    # print(str(lng([[1,1],[2,1],[3,None]])))
    # print(str(lng([[1,1],[2,1],[3,None]])))

    # assert str(s.copyRandomList(lng([]))) == str(lng([]))
    # a = lng([[1,1],[2,1]])
    # b = lng([[1,1],[2,1]])
    a = lng([[7,None],[13,0],[11,4],[10,2],[1,0]])
    b = lng([[7,None],[13,0],[11,4],[10,2],[1,0]])
    print(f'---- A ----\n{a}\n')
    print(f'---- B ----\n{a}\n')
    assert str(s.copyRandomList(a)) == str(b)
