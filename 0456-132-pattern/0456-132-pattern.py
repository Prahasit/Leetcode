class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # we use monotonically decreasing stack and also find minval for every index
        stack = [] #num, minleft
        n = len(nums)
        cur_min = nums[0]
        for i in range(1, n):
            while stack and nums[i] > stack[-1][0]:
                stack.pop()
            # i.e 'i' is min, top of stack is 'j' so it satisfies the condition
            if stack and nums[i] < stack[-1][0] and nums[i] > stack[-1][1]:
                return True 

            stack.append((nums[i], cur_min))
            cur_min = min(cur_min, nums[i])

        return False
        


