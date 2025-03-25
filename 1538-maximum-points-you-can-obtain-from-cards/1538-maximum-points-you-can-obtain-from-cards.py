class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # first take leftsum until k elements
        # then slowly reduce left element and add right element
        
        n = len(cardPoints)
        leftsum = sum(cardPoints[:k]) # sum of k elements
        max_points = leftsum
        rightsum = 0
        l, r = 0, n - 1
        for l in range(k):
            leftsum -= cardPoints[k - l - 1]
            rightsum += cardPoints[r]

            r -= 1 
            
            max_points = max(max_points, leftsum + rightsum)
            
        return max_points