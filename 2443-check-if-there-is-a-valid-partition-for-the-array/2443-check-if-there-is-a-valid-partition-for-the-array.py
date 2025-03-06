class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        def solve(idx):
            if idx == n:
                return True
            if idx in memo:
                return memo[idx]
            
            if idx + 1 < n and nums[idx] == nums[idx + 1]:
                if solve(idx + 2):
                    memo[idx] = True
                    return memo[idx]

            if idx + 2 < n and nums[idx] == nums[idx + 1] and nums[idx + 1] == nums[idx + 2]:
                if solve(idx + 3):
                    memo[idx] = True
                    return memo[idx]
            
            if idx + 2 < n and nums[idx]  + 1 == nums[idx + 1] and nums[idx + 1] + 1 == nums[idx + 2]:
                if solve(idx + 3):
                    memo[idx] = True
                    return memo[idx]
            
            memo[idx] = False
            return memo[idx]

        memo = {}
        n = len(nums)
        return solve(0)