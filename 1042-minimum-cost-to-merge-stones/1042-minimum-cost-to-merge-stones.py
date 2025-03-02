class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        '''In each move, we merge exactly k piles into 1 pile.
After one merge, we reduce the number of piles by k - 1 (k piles → 1 pile, so k-1 piles are removed).'''

        n = len(stones)

        if (n - 1) % (k - 1) != 0:
            return -1
        
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]
            
        @lru_cache(None)
        def dfs(i, j):
            if j - i + 1 < k:
                return 0
            min_cost = float('inf')
            for m in range(i, j, k - 1):
                min_cost = min(min_cost, dfs(i, m) + dfs(m + 1, j))

            if (j - i) % (k - 1) == 0:
                min_cost += prefix_sum[j + 1] - prefix_sum[i]

            return min_cost


        return dfs(0, n - 1)
