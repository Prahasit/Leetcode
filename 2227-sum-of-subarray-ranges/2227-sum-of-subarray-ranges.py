class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        #similar to sum of subarry minimum LC: 907
        # is is Sum of subarry Maximums - Sum of subarray minimums

        #minimum
        n = len(nums)
        smallest = 0
        stack1, stack2 = [], []
        pse = [-1] * n
        nse = [-1] * n
        MOD = (10 ** 9) + 7

        #finding next smaller element(NSE)
        for i in range(n - 1, - 1, -1):
            while stack1 and nums[i] <= nums[stack1[-1]]:
                stack1.pop()

            if not stack1:
                nse[i] = n
            else:
                nse[i] = stack1[-1]
            stack1.append(i)
        
        #finding previous smaller element (PSE)
        for i in range(n):
            while stack2 and nums[i] < nums[stack2[-1]]:
                stack2.pop()
            if not stack2:
                pse[i] = -1
            else:
                pse[i] = stack2[-1]
            
            stack2.append(i)
        print(nse)
        print(pse)
        for i in range(n):
            right = nse[i] - i
            left = i - pse[i]
            smallest = (smallest + nums[i] * left * right)
        

        #Maximum
        
        largest = 0
        stack3, stack4 = [], []
        pge = [-1] * n
        nge = [-1] * n
        MOD = (10 ** 9) + 7

        #finding next greater element(NGE)
        for i in range(n - 1, - 1, -1):
            while stack3 and nums[i] > nums[stack3[-1]]:
                stack3.pop()

            if not stack3:
                nge[i] = n
            else:
                nge[i] = stack3[-1]
            stack3.append(i)
        
        #finding previous Greater element (PGE)
        for i in range(n):
            while stack4 and nums[i] >= nums[stack4[-1]]:
                stack4.pop()
            if not stack4:
                pge[i] = -1
            else:
                pge[i] = stack4[-1]
            
            stack4.append(i)
        print(nge)
        print(pge)
        for i in range(n):
            right = nge[i] - i
            left = i - pge[i]
            largest = (largest + nums[i] * left * right)
        

        return largest - smallest