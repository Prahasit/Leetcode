class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # as its < not <=k what we can do is finding total num of subsets - >= k
        n = len(nums)
        l, r = 0, 0
        result = 0
        cur_prod = 1

        total_subarrays = n * (n + 1) // 2
        while r < n:
            cur_prod = cur_prod * nums[r]
            while cur_prod >= k and l <= r:
                result += n - r # asif we increase r we need add those elements also
                cur_prod = cur_prod / nums[l]
                l += 1

            
            r += 1
        

        return total_subarrays - result