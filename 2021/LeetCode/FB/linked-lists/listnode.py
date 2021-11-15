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
