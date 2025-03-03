class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        def dfs(node, dist, visit):
            visit[node] = True
            nei = edges[node]
            if nei != -1 and not visit[nei]:
                dist[nei] = dist[node] + 1
                dfs(nei, dist, visit)
                     

        n = len(edges)
        dist1 = [-1] * n
        dist2 = [-1] * n
        visit1, visit2 = [False] * n, [False] * n

        #initialize  the initialize nodesd distance to 0
        dist1[node1] = 0
        dist2[node2] = 0

        dfs(node1, dist1, visit1)
        dfs(node2, dist2, visit2)
        closest_node =  - 1
        min_dist = float('inf')

        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1:
                if min(dist1[i], dist2[i]) >= 0 and max(dist1[i], dist2[i]) < min_dist:
                    min_dist = max(dist1[i], dist2[i])
                    closest_node = i
        
        return closest_node
