from collections import defaultdict
from email.policy import default
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        The idea is that we're going to search for a '1' and once we find it, via dfs, we mark all nearby '1's as 0.
        We thus eliminate one island at a time, and just keep searching for more...
        """
        result = 0

        rows = len(grid)
        cols = len(grid[0])

        def eliminate(ridx, cidx):
            if (
                ridx < 0
                or cidx < 0
                or ridx >= rows
                or cidx >= cols
                or grid[ridx][cidx] != "1"
            ):
                return

            grid[ridx][cidx] = 0

            eliminate(ridx + 1, cidx)
            eliminate(ridx - 1, cidx)
            eliminate(ridx, cidx + 1)
            eliminate(ridx, cidx - 1)

        for ridx, r in enumerate(grid):
            for cidx, c in enumerate(r):
                if c == "1":
                    eliminate(ridx, cidx)

                    result = result + 1

        return result


if __name__ == "__main__":
    sol = Solution()

    def checkSolution(grid, expected, msg="Expected `{0}` but got `{1}`"):
        r = sol.numIslands(grid)
        print(flush=True)
        assert r == expected, msg.format(expected, r)

    checkSolution(
        grid=[
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],
        expected=1,
    )
