class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # if the element is smaller than the top of the stack, then pop it and then we can find pse and nse for that easily using one pass.
        # as first pop it and for thaat elemnt, nse is the the one occured as we only pop if the element < top of stack
        # we can find pse as it is next top of stack as we only add to stack if the elements are greater so we will get pse form it

        n = len(heights)
        stack = []
        max_area = 0
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                nse = i
                pse = stack[-1] if stack else - 1
                max_area = max(max_area, heights[index] * (nse - pse - 1))

            stack.append(i)
        
        # we need to look at remaining elementsin stack.
        while stack:
            nse = n # as if eleements are there in stack it means there is no nse for that element
            index = stack.pop()
            pse = stack[-1] if stack else -1
            max_area = max(max_area, heights[index] * (nse - pse - 1))
        
        return max_area

