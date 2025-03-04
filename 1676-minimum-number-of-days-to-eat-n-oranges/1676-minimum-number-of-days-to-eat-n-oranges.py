class Solution:
    def minDays(self, n: int) -> int:
        # for ech step 1 orange less is fine
        #other options include if multiple of 2 or multiple of 3 then.
        
        def dfs(num):
    
            if num <= 1:
                return num
            if num in dp:
                return dp[num]
            
            option2 = dfs(num// 2) + num % 2
            option3 = dfs(num//3) + num % 3

            dp[num] =  1 + min(option2, option3)

            return dp[num]
                
        dp = defaultdict(int)
        return dfs(n)
        