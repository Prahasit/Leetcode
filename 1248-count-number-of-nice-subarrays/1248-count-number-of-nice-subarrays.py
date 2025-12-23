class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def nicesubarrays(k):
            l, r = 0, 0
            count_odd = 0
            count_subarrays = 0

            while r < n:
                if nums[r] % 2 == 1:
                    count_odd += 1

                while count_odd > k:
                    if nums[l] % 2 == 1:
                        count_odd -= 1
                    l += 1

                count_subarrays += r - l + 1

                r += 1
            return count_subarrays

  
        n = len(nums)
        return nicesubarrays(k) - nicesubarrays(k - 1)
        