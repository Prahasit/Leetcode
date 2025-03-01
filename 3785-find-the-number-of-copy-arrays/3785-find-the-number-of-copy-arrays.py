class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
    
        n = len(original)
        left, right = bounds[0]
        for i in range(n):
            diff = original[i] - original[0]

            left = max(left, bounds[i][0] - diff)
            right = min(right, bounds[i][1] - diff)

            if left > right:
                return 0
        return right - left + 1