class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        visit = set()
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)
        def dfs(node):
            if node == destination:
                return True
            visit.add(node)
            for nei in adj_list[node]:
                if nei not in visit:  
                    if dfs(nei):
                        return True
            return False

        return dfs(source)
        