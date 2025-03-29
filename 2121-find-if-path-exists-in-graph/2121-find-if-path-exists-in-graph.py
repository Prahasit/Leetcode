class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)
        
        q = deque()
        q.append((source))
        visit = set()
        visit.add(source)

        while q:
            node = q.popleft()
            if node == destination:
                return True
            for nei in adj_list[node]:
                if nei not in visit:
                    visit.add(nei)
                    q.append(nei)

        return False