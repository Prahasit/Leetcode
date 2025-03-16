class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        freq = Counter(nums)
        for key, val in freq.items():
            if val > 1:
                temp = key
        nums_set = set(nums)
        for i in range(1, n + 1):
            if i not in nums_set:
                return [temp, i]

