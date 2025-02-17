class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # source = 0, destination = n - 1
        result = []
        temp = []
        def dfs(node):
            if node == len(graph) - 1:
                result.append(temp[:])
            
            for nei in graph[node]:
                temp.append(nei)
                dfs(nei)
                temp.pop()

        temp.append(0)
        dfs(0)
        return result