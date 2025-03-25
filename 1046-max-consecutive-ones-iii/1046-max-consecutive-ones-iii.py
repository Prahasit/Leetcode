class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # no to flip --> just count number of k '0's in th window

        n = len(nums)
        l, r = 0, 0
        zeroes = 0
        maxlen = 0
        while r < n:
            if nums[r] == 0:
                zeroes += 1
            if zeroes > k:
                if nums[l] == 0:
                    zeroes -= 1
                    l += 1
                else:
                    l += 1

            else:
                maxlen = max(maxlen, r - l + 1)

            r += 1
        return maxlen

