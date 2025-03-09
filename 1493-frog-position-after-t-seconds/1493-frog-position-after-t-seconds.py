class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        q = deque()
        visit = set()
        adj_list = defaultdict(list)
        out_degree = [0] * (n + 1)
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)
            out_degree[src] += 1
            out_degree[dst] += 1
        

        q.append((1, 1, 0)) #node, probability, level
        while q:
            for _ in range(len(q)):
                node, prob, level = q.popleft()
                visit.add(node)
                if node == target:
                    if level > t:
                        return 0
                    if level < t and out_degree[node] > 0:
                        return 0
                    else:
                        return prob

                for nei in adj_list[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append((nei, prob * (1 / out_degree[node]), level + 1 ))
                        out_degree[nei] -= 1

