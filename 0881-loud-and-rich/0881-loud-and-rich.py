class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        adj_list = defaultdict(list)
        for src, dst in richer:
            adj_list[dst].append(src)
        answer = [None] * len(quiet)
        def dfs(node):
            if answer[node] is None:
                answer[node] = node
                for nei in adj_list[node]:
                    temp = dfs(nei)
                    if quiet[temp] < quiet[answer[node]]:
                        answer[node] = temp
            return answer[node]
            

        for i in range(len(quiet)):
            answer[i] = dfs(i)
        return answer

        
        
        