from typing import List

# https://leetcode.com/problems/search-a-2d-matrix/
"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        So basic idea is that since each row is strictly greater than the preceeding row, it's like if we combined
        all rows into one giant row... it'd just be a single sorted array

        And then we can just use standard binary search from there

        We could potentially further optimize if we knew that say, the rows were a lot longer than there were # of
        columns... in which case might be better to binary search to find the correct row first, and then search within
        that row itself.
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        i = 0
        j = m * n - 1

        while i <= j:
            pivot = (i + j) // 2

            print(
                f"i:{i} j:{j} M:{m} N:{n} matrix[r:{pivot // m}][c:{pivot % n}] of {matrix}"
            )

            cur = matrix[pivot // n][pivot % n]

            if cur == target:
                return True
            elif cur < target:
                i = pivot + 1
            else:
                j = pivot - 1

        return False


if __name__ == "__main__":
    s = Solution()

    def checkSolution(matrix, target, expected, msg="Expected `{0}` but got `{1}`"):
        r = s.searchMatrix(matrix, target)
        assert r == expected, msg.format(expected, r)

    # checkSolution(
    #     matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
    #     target=3,
    #     expected=True,
    # )

    # checkSolution(
    #     matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
    #     target=13,
    #     expected=False,
    # )

    checkSolution(
        matrix=[[1, 1]],
        target=2,
        expected=False,
    )
