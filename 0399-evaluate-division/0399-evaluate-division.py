class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        result = []
        adj_list = defaultdict(list)
        for i, (src, dst) in enumerate(equations):
            adj_list[src].append((dst, values[i]))
            adj_list[dst].append((src, 1 / values[i]))
        
        def bfs(source, destination):
            
            if source not in adj_list:
                return - 1
            q = deque()
            q.append((1, source))
            visit= set()
            visit.add(source)
            while q:
                val, node = q.popleft()
                
                if node == destination:
                    return val
                for nei, w in adj_list[node]:
                    if nei not in visit:
                        q.append((val * w, nei))
                        visit.add(nei)
            return - 1
        for q in queries:
            source = q[0]
            destination = q[1]
            result.append(bfs(q[0], q[1]))

        return result

