class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        #just reverse the edges and find the edges whic are reachable

        #reversing the nodes
        adj_list = defaultdict(list)
        for src, dst in edges:
            adj_list[dst].append(src)
        
        def dfs(node):
            visit.add(node)
            for nei in adj_list[node]:
                if nei not in visit:
                    dfs(nei)

        answer = []
        for i in range(n):
            l = []
            visit = set() # all visited nodes are here and so can add it to the result      
            dfs(i)
            for node in range(n):
                if node == i:
                    continue
                if node in visit:
                    l.append(node)
            answer.append(l)

        return answer

        