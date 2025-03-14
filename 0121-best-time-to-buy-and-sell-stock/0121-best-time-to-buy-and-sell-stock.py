class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        least_price = prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] - least_price)
            if prices[i] < least_price:
                least_price = prices[i]

        return res

            
        