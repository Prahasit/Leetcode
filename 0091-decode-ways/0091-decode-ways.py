class Solution:
    def numDecodings(self, s: str) -> int:
        count = 0
        n = len(s)
    
        def solve(idx):
            if idx >= n:
                return 1
            if s[idx] == '0':
                return 0
            if idx in memo:
                return memo[idx]
                
            split = solve(idx+1)

            not_split = 0
            if idx + 1 < n and int(s[idx:idx+2]) <= 26:
                not_split = solve(idx + 2)

            memo[idx] = split + not_split
            return memo[idx]

        memo = {}
        return solve(0)