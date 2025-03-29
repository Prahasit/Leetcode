class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj_list = defaultdict(list)
        for src, dst in relations:
            adj_list[src - 1].append(dst - 1)

        @lru_cache(None)
        def dfs(node):
            temp = 0
            for nei in adj_list[node]:
                temp = max(temp, dfs(nei))

            if not adj_list[node]:
                return time[node]
            return temp + time[node]
        res = 0
        for i in range(n):
            res = max(res, dfs(i))

        return res
        
        


        