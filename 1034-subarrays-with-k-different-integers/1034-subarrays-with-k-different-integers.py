class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def subarray(k):
            freq = defaultdict(int)
            l, r = 0, 0
            result = 0

            while r < n:
                freq[nums[r]] += 1
                
                while len(freq) > k:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l += 1

                result += r - l + 1
                r += 1

            return result

        return subarray(k) - subarray(k - 1)