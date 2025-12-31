class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        count = 0
        adj_list = [[] for _ in range(len(isConnected))]

        for r in range(len(isConnected)):
            for c in range(len(isConnected)):
                if isConnected[r][c] == 1 and r != c:
                    adj_list[r].append(c)
                    adj_list[c].append(r)

        def dfs(node):
            visited[node] = True
            for nei in adj_list[node]:
                if not visited[nei]:
                    dfs(nei)

        for i in range(len(isConnected)):
            if not visited[i]:
                count += 1
                dfs(i)
        return count

