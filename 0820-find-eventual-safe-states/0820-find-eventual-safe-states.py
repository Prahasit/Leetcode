class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #reverse the adjacenct lit nad apply toposort.
        # as instad of finding the terminal nodes. if we can start from terminal nodes, it is easy

        n = len(graph)
        indegree = [0] * n
        reverse_list = defaultdict(list)
        res = []

        for i in range(n):
            for nei in graph[i]:
                reverse_list[nei].append(i)
                indegree[i] += 1
                
        # now apply toposort
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            res.append(node)
            
            for nei in reverse_list[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        res.sort()
        return res