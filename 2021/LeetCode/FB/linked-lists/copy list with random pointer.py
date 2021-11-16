from listnode import Node
from typing import *

debug = False
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        global debug

        if head is None:
            if debug: print(f'head<{head}> == first<{None}>')
            return None

        nodemap = {} # orig_node -> orig_idx
        idxmap = {} # orig_idx -> new node

        o = Node(0)
        first = o
        idxmap[0] = first

        pointer = head

        idx = 0
        while pointer is not None:
            if not (pointer in nodemap):
                nodemap[pointer] = idx

            target_value = pointer.val
            target_random = pointer.random

            print(f'target_value: {target_value}, target_random: {target_random}')
            node_random = None
            if not (target_random is None):
                if not (target_random in idxmap):
                    node_random = idxmap[target_random] = Node(0)

            curr = None
            if not (idx in idxmap):
                idxmap[idx] = curr = Node(target_value, node_random)
            else:
                curr = idxmap[idx]
                curr.val = target_value
                curr.random = node_random

            next_idx = idx + 1
            target_next = None
            if pointer.next is not None:
                if not (next_idx in idxmap):
                    idxmap[next_idx] = target_next = Node(0)
                else:
                    target_next = idxmap[next_idx]

            curr.next = target_next

            idx = next_idx
            pointer = pointer.next

        if debug: print(f'head<{head}> == first<{first}>')
        return first


if __name__ == '__main__':
    debug = True
    s = Solution()

    lng = Node.genFromList

    # print('test')
    # print(str(lng([[1,1],[2,1],[3,None]])))
    # print(str(lng([[1,1],[2,1],[3,None]])))

    # assert str(s.copyRandomList(lng([]))) == str(lng([]))
    a = lng([[1,1],[2,1]])
    b = lng([[1,1],[2,1]])
    print(f'---- A ----\n{a}\n')
    print(f'---- B ----\n{a}\n')
    assert str(s.copyRandomList(a)) == str(b)
