class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxleft = [0] * n
        maxright = [0] * n

        maxleft[0] = height[0]
        for i in range(1, n):
            maxleft[i] = max(maxleft[i - 1], height[i])
        
        maxright[n - 1] = height[n - 1]
        for i in range(n - 2, 0, -1):
            maxright[i] = max(maxright[i + 1], height[i])

        res = 0
        for i in range(n):
            if min(maxleft[i], maxright[i]) - height[i] > 0:
                res += min(maxleft[i], maxright[i]) - height[i]
        return res
