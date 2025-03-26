class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #directly finding == goal is difficult as if goal comes, there will be ambiguity wherther to update r or l as if we update one some cases will be missed. # fo example check for example 1 you will get to know
        # So what we can do is find the algorith for <= goal and then find for <= goal - 1 and subtract them i.e goal - (goal - 1) will will the answer

        def subarraysum(goal):
            l, r = 0, 0
            count = 0
            cur_sum = 0
            if goal < 0:
                return 0
            while r < n:
                cur_sum += nums[r]
                while cur_sum > goal:
                    cur_sum -= nums[l]
                    l += 1
                count += (r - l + 1)

                r += 1
            return count


        n = len(nums)
        return subarraysum(goal) - subarraysum(goal - 1)

            
