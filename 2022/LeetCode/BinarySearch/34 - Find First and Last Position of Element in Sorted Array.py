from typing import List


NOT_FOUND = -1
NOT_FOUND_ARR = [NOT_FOUND, NOT_FOUND]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        global NOT_FOUND_ARR

        # find the target if we can...
        start = self._findStart(nums, target)
        if start == NOT_FOUND:
            print(f"! Start Not Found => result: {NOT_FOUND_ARR}")
            return NOT_FOUND_ARR

        end = self._findEnd(nums, target)

        return [start, end]

    def _findStart(self, nums: List[int], target: int) -> int:
        return self._findStartEnd(nums, target, find_start=True)

    def _findEnd(self, nums: List[int], target: int) -> int:
        return self._findStartEnd(nums, target, find_start=False)

    def _findStartEnd(self, nums: List[int], target: int, find_start: bool) -> int:
        """
        This will find the start or end of the target sequence in nums, depending on if find_start is True or False
        """
        i = 0
        j = len(nums) - 1

        res = NOT_FOUND
        while i <= j:
            pivot = (i + j) // 2
            cur = nums[pivot]

            print(
                f"{('start' if find_start else 'end')} -- i:{i} j:{j} pivot:{pivot} cur:{cur} | {target} in {nums}"
            )

            if cur == target:
                # at this point we know the value at pivot is equal to our target
                if find_start:
                    if pivot == i or nums[pivot - 1] < target:
                        # we're at the start of our sequence
                        print(f"\t -> Start Found: {pivot}:{cur}")
                        return pivot

                    # otherwise keep searching
                    print(f"\t -> Continue Start Search: j:{j} -> {pivot-1}")
                    j = pivot - 1
                else:
                    if pivot == j or nums[pivot + 1] > target:
                        # we're at the end of our sequence
                        print(f"\t -> End Found: {pivot}:{cur}")
                        return pivot

                    # otherwise keep searching
                    print(f"\t -> Continue End Search: i:{i} -> {pivot+1}")
                    i = pivot + 1
            elif cur > target:
                print(f"\t -> {cur} > {target}: j:{i} -> {pivot-1}")
                j = pivot - 1
            else:
                print(f"\t -> {cur} <= {target}: i:{i} -> {pivot+1}")
                i = pivot + 1

        print(f"{('start' if find_start else 'end')} => result: {res}")
        return res


if __name__ == "__main__":
    s = Solution()

    def checkSolution(nums, target, expected, msg="Expected `{0}` but got `{1}`"):
        r = s.searchRange(nums, target)
        assert r == expected, msg.format(expected, r)

    checkSolution(nums=[5, 7, 7, 8, 8, 10], target=8, expected=[3, 4])
    checkSolution(nums=[5, 7, 7, 8, 8, 10], target=6, expected=NOT_FOUND_ARR)
    checkSolution(nums=[], target=0, expected=NOT_FOUND_ARR)
