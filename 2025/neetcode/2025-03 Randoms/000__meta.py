'''
Question 1: 
Consider the concept of a 'sorted, non-overlapping interval list' - which is an array of intervals that don't overlap with each other and are sorted by interval start.

Given two of these interval lists, return a 3rd interval list that is the union of the input interval lists.

Question Statement
For example:

Input:

List 1: {[1,2], [3,9]}
List 2: {[4,6], [8,10], [11,12]}

Output should be:

{[1,2], [3,10], [11,12]}

0   1   2   3   4   5   6   7   8   9  10  11  12

    [---]   [-----------------------]
                [-------]       [------]   [----]


Output:
    [---]   [--------------------------]   [----]

List1: [1,2] 
List2: [4,6]

List1: [3,9]
List2: [4,6]

=> [3,9]

List1: [3,9]
List2: [8,10]

=> [3,10]

List1: [3,10]
List2: [11,12]
'''

def solution(l1, l2):

    res = []

    i = 0 # l1
    j = 0 # l2
    while i < len(l1) and j < len(l2):
        si, ei = l1[i]
        sj, ej = l2[j]

        if si < sj:
            interval = l1[i]
            i += 1
        else:
            interval = l2[j]
            j += 1

        if len(res) == 0 or res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])

    while i < len(l1):
        interval = l1[i]

        if len(res) == 0 or res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])

        i += 1

    while j < len(l2):
        interval = l2[i]

        if len(res) == 0 or res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])

        j += 1

    return res

#if __name__ == '__main__':
'''
Question 2: 

Question:
Given a binary tree root node, write a function that returns the tree diameter (represented by this node).
Definition: diameter of a tree is the number of nodes on the longest path between two edge nodes.

Example:

            1 
          /   \
         2     3 
        /     / \
       4     5   6
                  \
                   7
4 - 2 - 1 - 3 - 6 -7: 
return 6 

            1 
          /   \
         2     3 
        / \     
       4   5    
      /     \
     6       7
    /         \
   8           9

8,6,4,2,5,7,9 = 7
'''

class TreeNode():
    def __init__():
        self.left
        self.right

def get_diameter(root):

    maxDiameter = 0

    def traverse(node):
        nonlocal maxDiameter
        
        if node is None:
            return 0
        
        leftSideHeight = self.traverse(node.left) 
        rightSideHeight = self.traverse(node.right)

        diameter = 1 + leftSideHeight + rightSideHeight 
        maxDiameter = max(maxDiameter, diameter) 

        return 1 + max(leftSideHeight, rightSideHeight)

    traverse(root)

    return maxDiameter

''''
            1                  1L=2,3
          /   \
         2     3               2=2,2
        /     / \
       4     5   6             4=1,1
                  \
                   7
''''