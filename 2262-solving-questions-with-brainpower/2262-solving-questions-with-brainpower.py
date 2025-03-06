class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        #recursion
        def recursion(idx):

            if idx >= n:
                return 0
            if idx in dp:
                return dp[idx]

            take = questions[idx][0] + recursion(idx + questions[idx][1] + 1)
            not_take = recursion(idx + 1)

            dp[idx] = max(take, not_take)
            return dp[idx]

        dp = {}
        n = len(questions)
        return recursion(0)