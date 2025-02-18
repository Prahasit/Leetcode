class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        count = 0
        adj_list = defaultdict(list)
        for src,dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)
        
        def dfs(node):
            component.add(node)
            for nei in adj_list[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)



        for i in range(n):
            if i not in visit:
                component = set()
                dfs(i)
                is_connect = True
                for node in component:
                    if len(adj_list[node]) != len(component) - 1:
                        is_connect = False
                        break
                if is_connect:
                    count += 1
        return count