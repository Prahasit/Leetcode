class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                      (2, 1), (2, -1), (-2, 1), (-2, -1)]

        memo = {}  # key: (moves_left, r, c) -> probability

        def dfs(moves_left: int, r: int, c: int) -> float:
            # out of board
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0.0

            # no moves left and still on board
            if moves_left == 0:
                return 1.0

            key = (moves_left, r, c)
            if key in memo:
                return memo[key]

            prob = 0.0
            for dr, dc in directions:
                prob += dfs(moves_left - 1, r + dr, c + dc)

            memo[key] = prob / 8.0
            return memo[key]

        return dfs(k, row, column)
