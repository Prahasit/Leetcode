class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        duplicate = Counter(nums)
        for i in duplicate:
            if duplicate[i] > 1:
                result.append(i)
        return result