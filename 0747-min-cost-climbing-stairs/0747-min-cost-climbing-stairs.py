class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def solve(ind):
            
            if ind == 0 or ind == 1:  
                return cost[ind]
            
            if ind in memo:
                return memo[ind]

            take1 = cost[ind] + solve(ind - 1) 
            take2 = cost[ind] + solve(ind - 2) 

            memo[ind] = min(take1, take2)
            return memo[ind]

        
        n = len(cost)
        memo = {}
        return min(solve(n - 1), solve(n - 2))
        