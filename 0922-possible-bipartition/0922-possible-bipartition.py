class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        #graph with even cycle is bipartite so can be divided
        #graph with odd ycle is not a bipartitie so cannot be divided

        adj_list = defaultdict(list)
        for src, dst in dislikes:
            adj_list[src - 1].append(dst - 1)
            adj_list[dst - 1].append(src - 1)

        colors = [-1] * n
        for i in range(n): 
            if colors[i] == - 1:
                q = deque([i])
                colors[i] = 0

            while q:
                node = q.popleft()
                for nei in adj_list[node]:
                    if colors[nei] == -1: # i.e not visited
                        colors[nei] = 1 - colors[node]
                        q.append(nei)
                    elif colors [nei] == colors[node]:
                        return False

        return True



        