class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        def dfs(visit, node, dist):
            visit[node] = True
            nei = edges[node]
            if nei != -1 and not visit[nei]:
                dist[nei] = dist[node] + 1
                dfs(visit, nei, dist)

        n = len(edges)
        dist1 = [-1] * n
        dist2 = [-1] * n
        dist1[node1] = 0
        dist2[node2] = 0

        visit1 = [False] * n
        visit2 = [False] * n

        dfs(visit1, node1, dist1)
        dfs(visit2, node2, dist2)

        min_dist = float('inf')
        closest = -1

        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1:
                if min(dist1[i], dist2[i]) >= 0 and max(dist1[i], dist2[i]) < min_dist:
                    min_dist = max(dist1[i], dist2[i])
                    closest = i
        

        return closest
