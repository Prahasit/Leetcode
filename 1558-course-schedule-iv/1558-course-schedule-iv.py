class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        result = []
        adj_list = defaultdict(list)
        for src, dst in prerequisites:
            adj_list[src].append(dst)
        
        def dfs(source, target):
            if source == target:
                return True
            visit[source] = True
            for nei in adj_list[source]:
                if not visit[nei]:
                    if dfs(nei, target):
                        return True

            return False


        for q in queries:
            visit = [False] * numCourses
            if dfs(q[0], q[1]): #finding dfs with the range of query
                result.append(True)
            else:
                result.append(False)
        return result

        
