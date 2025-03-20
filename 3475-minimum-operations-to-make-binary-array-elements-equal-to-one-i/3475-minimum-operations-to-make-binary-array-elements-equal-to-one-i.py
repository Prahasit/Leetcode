class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # if nums[i] == 0 apply the changes otherwise just move 
        n = len(nums)

        def solve(idx, count):
            if idx == n:
                return count
            if nums[idx] == 0:
                if idx  + 2 >= n:
                    return - 1
                for j in range(idx, idx + 3):
                    nums[j] ^= 1
                return solve(idx + 1, count + 1)
                
            else:
                return solve(idx + 1, count)

        
        return solve(0, 0)
        
        