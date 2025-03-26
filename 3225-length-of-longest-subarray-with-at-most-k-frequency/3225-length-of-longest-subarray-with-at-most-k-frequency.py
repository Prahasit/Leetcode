class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        l, r = 0, 0
        max_len = 0
        while r < n:
            freq[nums[r]] += 1
            while freq[nums[r]] > k:
                freq[nums[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

            r += 1

        return max_len

