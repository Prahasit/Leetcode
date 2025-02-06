from typing import List

class Solution:
    def __init__(self):
        self.n = None
        self.res = 0

    def countValidSelections(self, nums: List[int]) -> int:
        self.n = len(nums)

        def countValid(curr, nums):
            def helper(curr, nums, dir):
                # Simulate
                while 0 <= curr < self.n:
                    if nums[curr] == 0:
                        curr += dir
                    elif nums[curr] > 0:
                        nums[curr] -= 1
                        dir *= -1
                        curr += dir

                return all(x == 0 for x in nums)  # Returns 1 if all are zero, otherwise 0.

            return helper(curr - 1, nums[:], -1) + helper(curr + 1, nums[:], 1)

        for idx in range(self.n):
            if nums[idx] == 0:
                self.res += countValid(idx, nums)

        return self.res
