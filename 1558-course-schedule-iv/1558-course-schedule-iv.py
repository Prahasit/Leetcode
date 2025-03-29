class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj_list = defaultdict(list)
        for src, dst in prerequisites:
            adj_list[src].append(dst)
        
        def dfs(node, destination):
            if node == destination:
                return True

            visit[node] = True
            for nei in adj_list[node]:
                if not visit[nei]:
                    if dfs(nei, destination):
                        return True
            return False

        result = []
        for q in queries:
            visit = [False] * numCourses
            if dfs(q[0], q[1]):
                result.append(True)
            else:
                result.append(False)

        return result