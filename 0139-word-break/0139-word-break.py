class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #we find a way that 'leet', 'code' in leetcode--> 'leet' is there
        # it is better time complexity instead of fintinf each index in leetcode to  wordDict

        def solve(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            
            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i + len(w)] == w:
                    if solve(i + len(w)):
                        memo[i] = True
                        return memo[i]
            memo[i] = False
            return memo[i]

        memo = {}
        return solve(0)