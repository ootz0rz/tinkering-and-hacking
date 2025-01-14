class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def LN__ARRAY_TO_LL(arr=[]):
    if len(arr) == 0:
        return None
    
    start = ListNode()
    
    curNode = start
    for idx, e in enumerate(arr):

        curNode.val = e

        if (idx + 1) < len(arr):
            curNode.next = ListNode()
            curNode = curNode.next
    
    return start

def LN__LL_TO_ARRAY(head=None):
    # print("LL TO ARRAY: ", head)
    arr = []
    
    cnode = head
    while cnode is not None:
        # print(f"\t\t CUR: {cnode.val}")

        arr.append(cnode.val)
        cnode = cnode.next

    # print(" => ", arr)
    return arr

def TEST__ARRAY_TO_LL_AS_ARGS(*args):
    args = list(args)
    # print("array to ll [0]", args)
    for idx,a in enumerate(args):
        # print(f"\t{idx}: {a} -- {type(a)}")
        if type(a) == type([]):
            args[idx] = LN__ARRAY_TO_LL(a)
    # print("[1]", args)
    return args

def TEST__LL_TO_ARRAY_AS_ARGS(*args):
    args = list(args)
    print("ll to array [0]", args)
    for idx,a in enumerate(args):
        print(f"\t{idx}: {a} -- {type(a)}")
        if type(a) == ListNode:
            args[idx] = LN__LL_TO_ARRAY(a)
    print("=> [1]", args)
    return args