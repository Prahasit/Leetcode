

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)

        for q in queries:
            left = q[0]
            right = q[1]
            diff[left] += 1
            if right + 1 < n:
                diff[right + 1] -= 1
        
        current_dec = 0
        for i in range(n):
            current_dec += diff[i]
            nums[i] -= current_dec
            if nums[i] > 0:
                return False
        return True