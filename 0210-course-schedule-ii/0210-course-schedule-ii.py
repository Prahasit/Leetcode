class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = [0] * numCourses
        q = deque()
        visit = set()
        res = []
        for src, dst in prerequisites:
            adj_list[dst].append(src)
            indegree[src] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            res.append(node)
            visit.add(node)
            for nei in adj_list[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return res if len(visit) == numCourses else []
        