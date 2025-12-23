class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def kdifferentsubarray(k):
            l, r = 0, 0
            freq = defaultdict(int)
            count = 0
            while r < n:
                freq[nums[r]] += 1
                while len(freq) > k:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l += 1
                
                count += r - l + 1
                r += 1
            
            return count 

        n = len(nums)
        return kdifferentsubarray(k) - kdifferentsubarray(k - 1)