class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] <= height[r]:
                result = max(result, min(height[l], height[r]) * (r - l))
                l += 1

            else:
                result = max(result, min(height[l], height[r]) * (r - l))
                r -= 1

        return result

        