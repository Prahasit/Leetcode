class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_len = 0
        numset = set(nums)
        for i in numset:
            if i - 1 not in numset:
                longest = 0
                while i + longest in numset:
                    longest += 1
                    print(longest)
                max_len = max(max_len, longest)
        return max_len
