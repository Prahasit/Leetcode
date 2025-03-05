class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        dp = [-1] * (last_day + 1)
        travel_days = set(days) # converted to set for easy lookup i.e O(1) lookups
        def solve(curr_day):
            if curr_day > days[-1]:
                return 0
            if dp[curr_day] != - 1:
                return dp[curr_day]
            if curr_day not in  travel_days: #just skip
                dp[curr_day] =  solve(curr_day + 1)
                return dp[curr_day]
                
            one_day = costs[0] + solve(curr_day + 1)
            seven_days = costs[1] + solve(curr_day + 7)
            thirty_days = costs[2] + solve(curr_day + 30)

            dp[curr_day] = min(one_day, seven_days, thirty_days)
            return dp[curr_day]

        return solve(1)
