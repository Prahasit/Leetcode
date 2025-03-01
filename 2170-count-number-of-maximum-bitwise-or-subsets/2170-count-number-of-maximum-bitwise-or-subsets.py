class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        #maximum bitwise OR of an array is bitwise OR of the whole array as it is OR it takes into all elements and gives the max
        bit_OR = 0
        for num in nums:
            bit_OR |= num
        res = []
        def backtrack(subset, idx):
            if idx == len(nums):
                nonlocal count
                temp = 0
                for num in subset[:]:
                    temp |= num
                if temp == bit_OR:
                    count += 1
                return 
            subset.append(nums[idx])
            backtrack(subset, idx + 1)
            subset.pop()
            backtrack(subset, idx + 1)
        
        count = 0
        backtrack([],0)
        return count 

        