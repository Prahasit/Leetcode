class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def solve(total):
            # Base case: if the total reaches the target amount
            if total == amount:
                return 0

            # If the total exceeds the target amount, return infinity (invalid case)
            if total > amount:
                return float('inf')

            # If the result for this total is already computed, return it
            if total in memo:
                return memo[total]

            # Initialize the minimum number of coins to infinity
            min_coins = float('inf')

            # Try all possible coins
            for coin in coins:
                # Recursively solve for the new total
                result = solve(total + coin)
                # Update the minimum number of coins
                if result != float('inf'):
                    min_coins = min(min_coins, result + 1)

            # Store the result in the memoization dictionary
            memo[total] = min_coins
            return min_coins

        # Start the recursion with total = 0
        result = solve(0)

        # If the result is still infinity, it means the amount cannot be made
        return result if result != float('inf') else -1