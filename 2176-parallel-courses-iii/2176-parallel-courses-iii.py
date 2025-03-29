class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj_list = defaultdict(list)
        indegree = [0] * n
        max_months = [0] * n
        for src, dst in relations:
            adj_list[src - 1].append(dst - 1)
            indegree[dst - 1] += 1
        q = deque()
        
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                max_months[i] = time[i]
        
        while q:
            node = q.popleft()

            for nei in adj_list[node]:
                max_months[nei] = max(max_months[nei], max_months[node] + time[nei])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        
        return max(max_months)

        