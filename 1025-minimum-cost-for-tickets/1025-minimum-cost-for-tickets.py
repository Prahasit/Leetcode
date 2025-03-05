class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        dp = [0] * (last_day + 1)
        travel_days = set(days) # converted to set for easy lookup i.e O(1) lookups
        for curr_day in range(1, last_day + 1):

            if curr_day not in travel_days: #just skip
                dp[curr_day] =  dp[curr_day - 1]
                
            else:
                one_day = costs[0] + dp[curr_day - 1]
                seven_days = costs[1] + dp[max(0,curr_day - 7)]
                thirty_days = costs[2] + dp[max(0,curr_day - 30)]

                dp[curr_day] = min(one_day, seven_days, thirty_days)
            

        return dp[last_day]
