class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        # do it like take node 0 and check whether all nodes are reachabale or not
        # so for that reverse the node

        adj_list = defaultdict(list)
        for src, dst, w in edges:
            adj_list[dst].append((src, w))
        res = 0
        visit = set()
        pq = [(0, 0)] #weight, node

        while pq:
            w, node = heapq.heappop(pq)
            if node in visit:
                continue
            
            visit.add(node)
            res = max(res, w)
            for nei, wei in adj_list[node]:
                heapq.heappush(pq,(wei, nei))

        # if all elementsi n visit then return the max edge weight or else - 1
        if len(visit) == n:
            return res
        else:
            return - 1


        