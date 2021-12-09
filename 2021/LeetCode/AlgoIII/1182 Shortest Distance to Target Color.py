# https://leetcode.com/problems/find-a-peak-element-ii/submissions/
from typing import *

debug = False

MAX_VAL = 5 * (10**4) + 1

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        global debug, MAX_VAL

        if debug: print(f'colors: {colors}, queries: {queries}')

        # the basic idea is that we will generate a map in the form of m[i][j]
        # where i is an index, and j is a color
        #
        # this map will tell us at index i, how many steps away color j is from that index
        #
        # to do this we go through the colors list from start to end, and keep track of how
        # far away each color was from the current index. but this only tells us the distance
        # in one direction, so have to do the same thing again but search from end to start
        # and update values if they're smaller
        #
        # once that's done, we just loop through our queries and spit out the values
        #
        # queries is in the format [idx, color]

        map = []

        # search forwards
        d1 = d2 = d3 = -1
        idx = 0
        while idx < len(colors):
            cur_val = colors[idx]

            # increment distances, only if we've already found one of the vals before
            if d1 != -1: d1 = d1 + 1
            if d2 != -1: d2 = d2 + 1
            if d3 != -1: d3 = d3 + 1

            # if we encounter our own color, reset to 0
            if cur_val == 1: d1 = 0
            if cur_val == 2: d2 = 0
            if cur_val == 3: d3 = 0

            # update map with current values
            map.append([d1, d2, d3])

            idx = idx + 1

        if debug:
            import json
            print('---\ngenerated map [0]: ')
            print(json.dumps(map, sort_keys=True, indent=2))

        # search backwards
        d1 = d2 = d3 = MAX_VAL
        idx = len(colors) - 1
        while idx >= 0:
            cur_val = colors[idx]

            # increment distances, only if we've already found one of the vals before
            if d1 < MAX_VAL: d1 = d1 + 1
            if d2 < MAX_VAL: d2 = d2 + 1
            if d3 < MAX_VAL: d3 = d3 + 1

            # if we encounter our own color, reset to 0
            if cur_val == 1: d1 = 0
            if cur_val == 2: d2 = 0
            if cur_val == 3: d3 = 0

            # update map with current values if smaller than existing
            m1 = map[idx][0]
            m2 = map[idx][1]
            m3 = map[idx][2]
            if d1 < MAX_VAL and (m1 == -1 or m1 >= d1): map[idx][0] = d1
            if d2 < MAX_VAL and (m2 == -1 or m2 >= d2): map[idx][1] = d2
            if d3 < MAX_VAL and (m3 == -1 or m3 >= d3): map[idx][2] = d3

            idx = idx - 1

        if debug:
            import json
            print('---\ngenerated map [1]: ')
            print(json.dumps(map, sort_keys=True, indent=2))

        o = []
        for idx, col in queries:
            if idx < len(map):
                o.append(map[idx][col - 1])
            else:
                o.append(-1)

        return o


if __name__ == '__main__':
    debug = True
    s = Solution()

    # r = s.shortestDistanceColor([1, 2], [[0, 3]])
    # print(f'{r}')

    r = s.shortestDistanceColor([1,1,2,1,3,2,2,3,3], [[1,3],[2,2],[6,1]])
    print(f'{r}')

    # r = s.shortestDistanceColor([1, 2], [[0, 3]])
    # print(f'{r}')
