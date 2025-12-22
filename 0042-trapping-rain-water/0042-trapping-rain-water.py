class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0
        for i in range(n):
            maxleft= maxright = height[i]

            for j in range(0, i):
                maxleft = max(maxleft, height[j])
            
            for j in range(i + 1, n):
                maxright = max(maxright, height[j])

            res += min(maxleft, maxright) - height[i] 
        return res
