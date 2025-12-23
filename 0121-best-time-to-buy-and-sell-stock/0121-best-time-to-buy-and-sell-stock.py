class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        least = prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - least)
            if prices[i] < least:
                least = prices[i]

        return profit
