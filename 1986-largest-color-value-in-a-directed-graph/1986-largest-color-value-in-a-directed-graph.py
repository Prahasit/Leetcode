class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # there will be only 26 colors
        n = len(colors)
        indegree = [0] * n
        adj_list = defaultdict(list)
        for src, dst in edges:
            adj_list[src].append(dst)
            indegree[dst] += 1
        
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        # keeps track of the maximum occurrences of each color along a path to a given node
        counts = [[0] * 26 for _ in range(n)] 
        for i in range(n):
            counts[i][ord(colors[i]) - ord('a')] += 1

        max_count = 0
        visited = 0

        while q:
            node = q.popleft()
            visited += 1

            for nei in adj_list[node]:
                for i in range(26):
                    counts[nei][i] = max(counts[nei][i], counts[node][i] + (ord(colors[nei]) - ord('a') == i))
                
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            max_count = max(max_count, max(counts[node]))
        # we indirectly also check for cycle a if it is ccyle indegree of nodes will not 0 ani visited is < n
        return max_count if visited == n else - 1
