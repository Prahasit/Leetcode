class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints[:k])
        max_points = total

        for i in range(k):
            total -= cardPoints[k -i -1]
            total += cardPoints[n - 1 - i]

            max_points = max(max_points, total)


        return max_points