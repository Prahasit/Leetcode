class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        indegree = [0] * numCourses
        for src, dst in prerequisites:
            adj_list[dst].append(src)
            indegree[src] += 1

        visit = set()
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            visit.add(node)
            for nei in adj_list[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return numCourses == len(visit)