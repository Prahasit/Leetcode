class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        # dp[i][j] will store the number of valid strings of length i ending with vowels[j]
        dp = [[0] * 5 for _ in range(n + 1)]
        
        # Base case: There is 1 string of length 1 for each vowel
        for j in range(5):
            dp[1][j] = 1
        
        # Fill the dp table
        for i in range(2, n + 1):
            for j in range(5):
                # dp[i][j] is the sum of dp[i-1][0] + dp[i-1][1] + ... + dp[i-1][j]
                dp[i][j] = sum(dp[i-1][:j+1])
        
        # The answer is the sum of all dp[n][0], dp[n][1], dp[n][2], dp[n][3], dp[n][4]
        return sum(dp[n])