class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        max_points = 0
        left_sum = sum(cardPoints[:k])
        right_sum = 0

        max_points = max(max_points, left_sum)
        
        for i in range(k):
            left_sum -= cardPoints[k - i - 1]
            right_sum += cardPoints[n - i - 1]

            max_points = max(max_points, left_sum + right_sum)

        return max_points
        