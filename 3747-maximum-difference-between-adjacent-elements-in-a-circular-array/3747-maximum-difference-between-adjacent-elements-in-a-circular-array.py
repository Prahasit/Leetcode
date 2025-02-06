class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        adj_dist = 0
        for i in range(1, n):
            adj_dist = max(adj_dist, abs(nums[i] - nums[i - 1]))
        return max(adj_dist, abs(nums[0] - nums[n - 1]))