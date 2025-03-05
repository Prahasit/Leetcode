class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        tickets.sort(reverse =True)
        for src, dst in tickets:
            adj_list[src].append(dst)

        def dfs(src):
            while adj_list[src]:
                dst = adj_list[src].pop()
                dfs(dst)
            res.append(src)

        res = []
        dfs("JFK")
        return res[::-1]


        