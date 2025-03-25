class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        l, r = 0, 0
        max_sub_sum = float('-inf')
        sub_sum = 0
        for i in range(k):
            sub_sum += nums[i]
            r += 1

        max_sub_sum = max(max_sub_sum, sub_sum / k)

        while r < n:
            sub_sum += nums[r]
            sub_sum -= nums[l]

            max_sub_sum = max(max_sub_sum, sub_sum / k)

            r += 1
            l += 1
        
        return max_sub_sum
