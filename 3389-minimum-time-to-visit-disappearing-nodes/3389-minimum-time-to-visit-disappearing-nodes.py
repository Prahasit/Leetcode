class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        adj_list = defaultdict(list)
        for edge in edges:
            adj_list[edge[0]].append((edge[1], edge[2]))
            adj_list[edge[1]].append((edge[0], edge[2]))
        
        dist = [float('inf')] * n
        dist[0] = 0
        heap = []
        heapq.heappush(heap, (0 , 0)) #distance, node

        while heap:
            distance, node = heapq.heappop(heap)
            if distance > dist[node]:
                continue
            for nei, d in adj_list[node]:
                if distance + d < dist[nei] and distance + d < disappear[nei]:
                    dist[nei] = distance + d
                    heapq.heappush(heap, (dist[nei], nei))
        
        for i in range(n):
            if dist[i] == float('inf'):
                dist[i] = -1
        
        return dist