class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(node):
            
            if node == n - 1:
                result.append(l[:])
            for nei in graph[node]:
                l.append(nei)
                dfs(nei)
                l.pop()

            

        n = len(graph)
        l = []
        l.append(0)
        result = []
        dfs(0)
        return result