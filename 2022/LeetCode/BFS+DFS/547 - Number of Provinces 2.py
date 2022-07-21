# https://leetcode.com/problems/number-of-provinces/

from typing import List


CONNECTED = 1
EMPTY = 0


def explore(x, isConnected, used_cities):
    used_cities[x] = True

    for iy, cell in enumerate(isConnected[x]):
        if not (iy in used_cities) and cell == CONNECTED:
            explore(iy, isConnected, used_cities)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0

        # since isconnected is symmetrical along the diagonal, we only care about the idx of the current city
        # we're on... so used_cities[x] = True means x is already part of a province
        used_cities = {}

        for ix, xrow in enumerate(isConnected):
            if not (ix in used_cities):
                explore(ix, isConnected, used_cities)
                provinces = provinces + 1

        return provinces


if __name__ == "__main__":
    s = Solution()

    def checkSolution(isConnected, expected, msg="Expected `{0}` but got `{1}`"):
        r = s.findCircleNum(isConnected)
        assert r == expected, msg.format(expected, r)

    checkSolution(
        isConnected=[[1, 1, 0], [1, 1, 0], [0, 0, 1]],
        expected=2,
    )

    checkSolution(
        isConnected=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        expected=3,
    )
