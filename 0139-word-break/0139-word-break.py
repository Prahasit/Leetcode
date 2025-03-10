class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #we find a way that 'leet', 'code' in leetcode--> 'leet' is there
        # it is better time complexity instead of fintinf each index in leetcode to  wordDict

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]