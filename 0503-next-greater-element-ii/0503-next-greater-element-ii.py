class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        res = [-1] * n
        k = 2 * n
        for i in range(k - 1, - 1, - 1):
            idx = i % n
            while stack and nums[idx] >= stack[-1]:
                stack.pop()
        
            
            if i < n:
                if not stack:
                    res[i]  = -1
                else:
                    res[i] = stack[-1]

            stack.append(nums[idx])

        return res