class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        adj_list = defaultdict(list)
        indegree = [0] * n
        max_time = [0] * n
        for src, dst in relations:
            adj_list[src - 1].append(dst - 1)
            indegree[dst - 1] += 1
        
        q = deque()
        for node in range(n):
            if indegree[node] == 0:
                q.append(node)
                max_time[node] = time[node]
        while q:
            node = q.popleft()
            for nei in adj_list[node]:
                max_time[nei] = max(max_time[nei], max_time[node] + time[nei])

                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return max(max_time)


        