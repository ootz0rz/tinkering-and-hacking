import queue
from typing import List
from collections import defaultdict

"""
# BFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        result = 0

        N = len(isConnected)  # NxN

        visited = {}

        queue = []

        for cidx in range(N):
            if cidx in visited:
                continue

            queue.append(cidx)
            while len(queue) > 0:
                city = queue.pop()
                visited[city] = True

                for conn_idx in range(N):
                    if isConnected[city][conn_idx] == 1 and conn_idx not in visited:
                        queue.append(conn_idx)

            result += 1

        return result
"""


# DFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        result = 0
        N = len(isConnected)  # NxN

        visited = {}

        def DFS(idx):
            for j in range(N):
                if j in visited:
                    continue

                if isConnected[idx][j] == 1:
                    visited[j] = True
                    DFS(j)

        for idx in range(N):
            if idx in visited:
                continue

            DFS(idx)
            result += 1

        return result


if __name__ == "__main__":
    sol = Solution()

    def checkSolution(isConnected, expected, msg="Expected `{0}` but got `{1}`"):
        r = sol.findCircleNum(isConnected)
        print(flush=True)
        assert r == expected, msg.format(expected, r)

    checkSolution(isConnected=[[1, 1, 0], [1, 1, 0], [0, 0, 1]], expected=2)
    checkSolution(isConnected=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], expected=3)
    checkSolution(
        isConnected=[[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]], expected=1
    )
