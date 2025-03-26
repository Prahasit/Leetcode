class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # doing it the reverse way
        target = sum(nums) - x
        if target < 0:
            return -1  # If total sum is smaller than x, it's impossible

        n = len(nums)
        l = 0
        cur_sum = 0
        max_len = -1  # To store the longest subarray sum == target

        for r in range(n):
            cur_sum += nums[r]

            while cur_sum > target and l <= r:
                cur_sum -= nums[l]
                l += 1

            if cur_sum == target:
                max_len = max(max_len, r - l + 1)

        return n - max_len if max_len != -1 else -1