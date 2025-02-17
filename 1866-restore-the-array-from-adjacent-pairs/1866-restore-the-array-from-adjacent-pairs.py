class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        #as all are adjacent pairs they are are doubly linked list
        #we need to start at one end i.e the lement which appears only once in adjacent pairs
        res = []
        adj_list = defaultdict(list)
        for src,dst in adjacentPairs:
            adj_list[src].append(dst)
            adj_list[dst].append(src)

        root = None
        for nodes in adj_list:
            if len(adj_list[nodes]) == 1:
                root = nodes
                break
        def dfs(node, prev):
            res.append(node)
            for nei in adj_list[node]:
                if nei != prev: #i.e not the parent it came from
                    dfs(nei, node)
        
        dfs(root, None)
        return res
        
        