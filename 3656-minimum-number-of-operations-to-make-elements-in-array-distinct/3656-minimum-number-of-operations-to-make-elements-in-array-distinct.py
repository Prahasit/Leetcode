class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        operations = 0
        for i in nums:
            freq[i] += 1

        while len(freq) < len(nums):
            removed = nums[:3]
            nums = nums[3:]
            
            for i in removed:
                freq[i] -= 1
                if freq[i] == 0:
                    del freq[i]

            operations += 1
        return operations
        
            
