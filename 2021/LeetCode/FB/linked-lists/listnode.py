debug = False
class Node:
    @staticmethod
    def genFromList(l=[]):
        global debug
        if len(l) == 0:
            return None

        idxmap = {} # idx -> node
        idx = 0

        node = Node(0)
        idxmap[idx] = node
        first = node

        if debug: print(f'GEN FROM LIST: {l}')

        while idx < len(l):
            target_val,target_random = l[idx]

            if debug: print(f'\t val: {target_val} rand: {target_random}')

            node = None
            if not (idx in idxmap):
                node = idxmap[idx] = Node(0)
                if debug: print(f'\t\t Create node with value {node.val}, idx {idx}, id {id(node)}')
            else:
                node = idxmap[idx]
                if debug: print(f'\t\t Retrieved node with value {node.val}, idx {idx}, id {id(node)}')
            node.val = target_val
            node.random_idx = target_random
            if debug: print(f'\t\t\t Set value of {idx} to {node.val}')

            node_random = None
            if not (target_random is None) and not (str(target_random).lower() == 'null'):
                if not (target_random in idxmap):
                    node_random = idxmap[target_random] = Node(0)
                    if debug: print(f'\t\t Create random target with value {node_random.val}, idx {target_random}, id {id(node_random)}')
                else:
                    node_random = idxmap[target_random]
                    if debug: print(f'\t\t Retrieved random node with value {node_random.val}, idx {target_random}, id {id(node_random)}')
            node.random = node_random
            if debug: print(f'\t\t\t Set reference of random node to {id(node.random)} via idx {target_random}')

            next_idx = idx + 1
            if next_idx < len(l):
                node_next = None
                if not (next_idx in idxmap):
                    node_next = idxmap[next_idx] = Node(0)
                else:
                    node_next = idxmap[next_idx]
                node.next = node_next
            if debug: print(f'\t\t --> Next Node: {None if node.next is None else id(node.next)}')

            idx = next_idx

        return first

    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None, random_idx = 0):
        self.val = int(x)
        self.next = next
        self.random = random
        self.random_idx = random_idx

    def __repr__(self):
        global debug
        if debug: print(f'\n__REPR__ GEN')
        sb = []
        idxmap = {} # node -> idx

        # gen map
        next = self
        idx = 0
        while next is not None:
            idxmap[id(next)] = idx

            if debug: print(f'add next<{id(next)}> at idx<{idx}>')

            next = next.next
            idx = idx + 1

        if debug: print(f'MAP: {idxmap}')

        # gen repr
        next = self
        while next is not None:
            idx = idxmap[id(next)]
            randidx = None
            if not (next.random is None) and id(next.random) in idxmap:
                randidx = idxmap[id(next.random)]

            sb.append(f'idx[{idx}] val[{next.val}] rand[{randidx}]')

            next = next.next

        if debug: print(f'__REPR__: {sb}')
        return sb

    def __str__(self):
        return 'ND' + str(self.__repr__())

class ListNode:
    @staticmethod
    def genFromList(l=[]):
        if len(l) == 0:
            return None

        node = ListNode()
        first = node

        idx = 0
        while idx < len(l):
            val = l[idx]

            node.val = val
            if (idx + 1) < len(l):
                node.next = ListNode()
                node = node.next

            idx = idx + 1
        # print(f"genFromList, list<{l}> result<{str(first)}>")

        return first

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        sb = []

        next = self
        while next is not None:
            sb.append(next.val)
            next = next.next

        return sb

    def __str__(self):
        return 'LL' + str(self.__repr__())
