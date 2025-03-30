class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list = defaultdict(list)
        for i, (src, dst) in enumerate(edges):
            adj_list[src].append((dst, succProb[i]))
            adj_list[dst].append((src, succProb[i]))

        prob = [0.0] * n
        prob[start_node] = 1
        q = deque()
        q.append((start_node, prob[start_node])) # node, probability

        while q:
            node, cur_prob = q.popleft()
            
            for nei, p in adj_list[node]:
                if cur_prob * p  > prob[nei]:
                    prob[nei] = cur_prob * p
                    q.append((nei, prob[nei]))

        return prob[end_node]
            


            