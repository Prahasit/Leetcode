class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list = defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj_list[src].append((dst, succProb[i]))
            adj_list[dst].append((src, succProb[i]))

        max_heap = [(-1, start_node)] # -1 as its minheap so -1 * 1 = -1
        visit = set()
        while max_heap:
            prob, node = heapq.heappop(max_heap)
            visit.add(node)

            if node == end_node:
                return -prob

            for nei, edge_prob in adj_list[node]:
                if nei not in visit:
                    heapq.heappush(max_heap, (prob * edge_prob, nei))
        return 0

        