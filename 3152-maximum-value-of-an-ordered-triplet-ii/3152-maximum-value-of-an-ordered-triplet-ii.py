class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = 0
        left_max = [0] * n
        right_max = [0] * n

        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i - 1])
            right_max[n - i - 1] = max(right_max[n- i], nums[n - i])

        for j in range(1, n - 1):
            max_val = max(max_val, (left_max[j] - nums[j]) * right_max[j])

        return max_val
        