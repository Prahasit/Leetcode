class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages, scores))  # Sort by age, then by score
        n = len(scores)
        dp = [0] * n

        for i in range(n):
            dp[i] = players[i][1]  # Base case: team with only this player
            for j in range(i):
                if players[j][1] <= players[i][1]:  # No conflict condition
                    dp[i] = max(dp[i], dp[j] + players[i][1])
        
        return max(dp)