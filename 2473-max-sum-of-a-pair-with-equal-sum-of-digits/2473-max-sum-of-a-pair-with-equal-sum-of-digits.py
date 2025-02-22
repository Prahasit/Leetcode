class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def SumDigits(num):
            rem = 0
            while num > 0:
                rem += num % 10
                num = num // 10
            return rem
        
        freq = {} # digit_sum : actual value
        res = -1
        for i in nums:
            digit_sum = SumDigits(i)
            if digit_sum in freq:
                old = freq[digit_sum]
                res = max(res, old + i)
                freq[digit_sum] = max(old, i)

            else:
                freq[digit_sum] = i
        
        
        return res



                