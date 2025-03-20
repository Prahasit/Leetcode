class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for key, val in freq.items():
            if val % 2 == 1:
                return False

        return True