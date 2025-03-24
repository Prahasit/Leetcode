class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #for every index basically need to find out PSE and NSE and answer is between it. calcuate liek this for element

        n = len(heights)
        stack1, stack2 = [], []
        pse = [-1] * n
        nse = [-1] * n

        # finding previous smaller element
        for i in range(n):
            while stack1 and heights[i] <= heights[stack1[-1]]:
                stack1.pop()
            
            if stack1:
                pse[i] = stack1[-1]
            else:
                pse[i] = - 1

            stack1.append(i)

        # finding next smaller element
        for i in range(n - 1, - 1, -1):
            while stack2 and heights[i] <= heights[stack2[-1]]:
                stack2.pop()
            if stack2:
                nse[i] = stack2[-1]
            else:
                nse[i] = n
            
            stack2.append(i)

        print(pse)
        print(nse)
        result = 0
        for i in range(n):
            result = max(result, heights[i] * (nse[i] - pse[i] - 1))
            print(result)
        return result