"""
Two single linked lists (length range 1 to 9999)，
adding the corresponding nodes of the two lists to get a 
number and store the number into the oupt single linked list.

Input lists:  L1 (5->9)； L2 ( 7->1->4)
Output list:  L (7->7->3)
Explanation：59+714= 773
"""

# gave https://pastebin.com/Yg8BsrMr


class Node:
    v = None
    next = None

    def __init__(self, v=None, next=None):
        self.v = v
        self.next = next

    def __str__(self):
        s = f"{self.v},"

        n = self.next
        while n is not None:
            s += f"{n.v},"
            n = n.next

        return s


def __add_LL(smaller, bigger, slen, blen):
    out_head = Node()

    # base case
    if (
        (smaller is not None)
        and (bigger is not None)
        and (smaller.next is None)
        and (bigger.next is None)
    ):
        out_head.v = smaller.v + bigger.v

        return out_head

    # recurse through largest until the remained is same size, and then
    # add the rest
    res = None
    if (smaller is not None) and (bigger is not None) and (slen == blen):
        # sizes are same, move ahead in both
        res = __add_LL(smaller.next, bigger.next, slen - 1, blen - 1)

        # add the carry on to the current nodes
        out_head.v = (smaller.v + bigger.v) + (res.v // 10)

    elif (smaller is not None) and (bigger is not None):
        # proceed along the bigger list
        res = __add_LL(smaller, bigger.next, slen, blen - 1)
        out_head.v = (smaller.v + bigger.v) + (res.v // 10)

    # apply the major part of the carry as our "next" node
    out_head.next = res
    res.v = res.v % 10

    return out_head


def add_LL(first, second):
    # calculate sizes
    flen = __LL_size(first)
    slen = __LL_size(second)

    # determine which list to traverse; bigger is primary
    res = None
    if flen > slen:
        res = __add_LL(second, first, slen, flen)
    else:
        res = __add_LL(first, second, flen, slen)

    # it's possible that the final first node output could be greater than 10 with carry,
    # so make sure we account for that
    if res.v >= 10:
        new_head = Node(res.v // 10)
        res.v = res.v % 10
        new_head.next = res

        return new_head

    return res


def __LL_size(head):
    s = 0
    h = head
    while h is not None:
        h = h.next
        s += 1

    return s


if __name__ == "__main__":

    L1 = Node(5, Node(9))
    L2 = Node(7, Node(1, Node(4)))

    print(f"Add: {L1}")
    print(f"Add: {L2}")

    print(f"Result: {add_LL(L1, L2)}")
