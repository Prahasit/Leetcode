class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for vals in freq.values():
            if vals > 1:
                return True
        return False