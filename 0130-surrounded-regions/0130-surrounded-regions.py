class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != "O":
                return
            
            board[r][c] = "*"

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)


        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i in [0, m - 1] or j in [0, n - 1]):
                    dfs(i ,j)


        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = "X"

        for i in range(m):
            for j in range(n):
                if board[i][j] == '*':
                    board[i][j] = "O"

        