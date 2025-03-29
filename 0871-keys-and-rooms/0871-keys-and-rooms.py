class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #similar to course schedule
        n = len(rooms)
        adj_list = defaultdict(list)
        indegree = [0] * n
        for i in range(n):
            for keys in rooms[i]:
                adj_list[i].append(keys)
                indegree[keys] += 1
        
        q = deque()
        visit = set()
        visit.add(0)
        q.append((0))
        
        while q:
            room = q.popleft()
            

            for adj_room in adj_list[room]:
                if adj_room not in visit:
                    visit.add(adj_room)
                    q.append(adj_room)


        return n == len(visit)