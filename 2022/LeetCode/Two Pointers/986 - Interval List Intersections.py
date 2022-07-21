# https://leetcode.com/problems/interval-list-intersections/


from typing import List


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        res = []

        i = 0
        j = 0

        while i < len(firstList) and j < len(secondList):
            left = max(firstList[i][0], secondList[j][0])
            right = min(firstList[i][1], secondList[j][1])

            if left <= right:
                res.append([left, right])

            if firstList[i][1] < secondList[j][1]:
                i = i + 1
            else:
                j = j + 1

        return res


if __name__ == "__main__":
    s = Solution()

    def checkSolution(
        firstList, secondList, expected, msg="Expected `{0}` but got `{1}`"
    ):
        r = s.intervalIntersection(firstList, secondList)
        assert r == expected, msg.format(expected, r)

    checkSolution(
        firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
        secondList=[[1, 5], [8, 12], [15, 24], [25, 26]],
        expected=[[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
    )
