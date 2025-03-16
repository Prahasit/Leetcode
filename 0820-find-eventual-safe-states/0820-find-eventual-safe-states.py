class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visit = [0] * n
        path_vis = [0] * n
        check = [0] * n

        def dfs(node):
            visit[node] = 1
            path_vis[node] = 1
            check[node] = 0

            for nei in graph[node]:
                if visit[nei] == 0:
                    if dfs(nei):
                        return True
                elif path_vis[nei] == 1:
                    return True

            path_vis[node] = 0
            check[node] = 1
            return False




        for i in range(n):
            if visit[i] == 0:
                dfs(i)
        result = []
        for i in range(n):
            if check[i] == 1:
                result.append(i)
        
        return result
            
            