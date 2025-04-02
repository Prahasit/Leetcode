class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # brute force
        n = len(nums)
        max_val = 0
        for i in range(n - 2):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    max_val = max(max_val, (nums[i] - nums[j]) * nums[k])

        return max_val
