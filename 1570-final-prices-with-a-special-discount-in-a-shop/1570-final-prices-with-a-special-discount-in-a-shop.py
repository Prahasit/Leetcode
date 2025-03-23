class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and prices[i] <= stack[-1][0]:
                val, idx = stack.pop()
                result[idx] = val - prices[i]

            stack.append((prices[i], i))

        while stack: # the reamining elements pop them like in first example 2, 3 will remain
            val, idx = stack.pop()
            result[idx] = val
        return result