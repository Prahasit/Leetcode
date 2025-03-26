class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
       # if we all odd as 1 and all even as 0 then it will be same as LC 930


        def subarraysum(k):

            l, r = 0, 0
            sub_sum = 0
            count  = 0
            while r < n:
                sub_sum += nums[r] % 2
                while sub_sum > k:
                    sub_sum -= nums[l] % 2
                    l += 1
                
                count += (r - l + 1)

                r += 1
            return count
            
        n = len(nums)
        return subarraysum(k) - subarraysum(k - 1)



