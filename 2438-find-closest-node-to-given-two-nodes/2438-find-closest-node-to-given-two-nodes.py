class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        def bfs(node, dist):
            q = deque()
            q.append(node)
            visit = [False] * n
            dist[node] = 0
            while q:
                node = q.popleft()
                if visit[node]:
                    continue
                visit[node] = True
                nei = edges[node]
                if nei != - 1 and not visit[nei]:
                    dist[nei] = dist[node] + 1
                    q.append(nei)

        n = len(edges)
        dist1 = [-1] * n
        dist2 = [-1] * n

        bfs(node1, dist1)
        bfs(node2, dist2)
        closest_node =  - 1
        min_dist = float('inf')

        for i in range(n):
            if min(dist1[i], dist2[i]) >= 0 and max(dist1[i], dist2[i]) < min_dist:
                min_dist = max(dist1[i], dist2[i])
                closest_node = i
        
        return closest_node
