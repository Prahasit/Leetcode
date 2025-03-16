class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj_list = defaultdict(list)
        q = deque()
        res = 0
        for i, node in enumerate(manager):
            if node != -1:
                adj_list[node].append(i)
            else:
                q.append((i, 0))
        
        while q:

            node, time = q.popleft()
            res = max(res, time)
            for nei in adj_list[node]:
                q.append((nei, time + informTime[node]))

        return res


        
        