# https://leetcode.com/problems/all-paths-from-source-to-target/

from typing import List, Optional
from collections import deque


def find_paths(cur_node, graph, goal, cur_path, paths):
    # print(f"find_paths: cur[{cur_node}] goal[{goal}] path[{cur_path}] paths[{paths}]")
    if cur_node == goal:
        # print(f"\tAdd new path: {cur_path} to {paths}")
        paths.append(list(cur_path))
        # print(f"\tAdded new path: {cur_path} to {paths}")
        return

    for node in graph[cur_node]:
        cur_path.append(node)
        find_paths(node, graph, goal, cur_path, paths)
        cur_path.pop()


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        last_node = len(graph) - 1

        paths = []
        # print(f"Paths[0]: {paths}")
        find_paths(0, graph, last_node, cur_path=[0], paths=paths)
        # print(f"Paths[1]: {paths}")

        return paths


if __name__ == "__main__":
    s = Solution()

    def checkSolution(graph, expected, msg="Expected `{0}` but got `{1}`"):
        print(f"\n\n----- graph: {graph}")

        r = s.allPathsSourceTarget(graph)

        assert len(r) == len(
            expected
        ), f"Expected outut len {len(expected)} but got {len(r)}. Expected: {expected} Result: {r}"

        # https://stackoverflow.com/questions/6105777/how-to-compare-a-list-of-lists-sets-in-python
        rset = set(map(tuple, r))
        eset = set(map(tuple, expected))

        diff = rset.symmetric_difference(eset)

        print(f"r: {rset} v e: {eset}")
        assert (
            len(diff) == 0
        ), f"Expected no differences, but got {len(diff)}:{diff} vs {len(eset)}:{eset}"

        print("Completed test case.")

    checkSolution(
        graph=[[1, 2], [3], [3], []],
        expected=[[0, 1, 3], [0, 2, 3]],
    )
