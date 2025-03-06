class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        
        for idx in range(n - 1, - 1, -1):

            take = questions[idx][0] + (dp[idx + questions[idx][1] + 1] if idx + 1 + questions[idx][1] < n else 0)
            not_take = dp[idx + 1]

            dp[idx] = max(take, not_take)

        
        return dp[0]