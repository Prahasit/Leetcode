class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        freq = Counter(nums)
        operations = 0
        while len(freq) < len(nums):
            nums = nums[3:]
            freq = Counter(nums)
            operations += 1

        return operations
        
            
