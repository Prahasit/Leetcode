class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # reversing the edges and finding reachability

        adj_list = defaultdict(list)
        result = []
        for src, dst in edges:
            adj_list[dst].append(src)

        
        def dfs(node):
            

            for nei in adj_list[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)


        for i in range(n):
            visit = set()
            l = []
            dfs(i)
            for node in visit:
                l.append(node)
            l.sort()
            result.append(l)

        return result
            
