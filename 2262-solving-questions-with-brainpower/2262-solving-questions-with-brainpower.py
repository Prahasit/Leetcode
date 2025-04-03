class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        def dfs(idx):
           

            if idx >= n:
                return 0
            
            if idx in memo:
                return memo[idx]
            take = questions[idx][0] + dfs(idx + questions[idx][1] + 1)
            not_take = dfs(idx + 1)

            memo[idx] = max(take, not_take)
            return memo[idx]

            

        n = len(questions)
        memo = {}
        return dfs(0)
        