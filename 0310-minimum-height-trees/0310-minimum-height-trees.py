class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #MST is like center of tree which is almost equal distance to left and right part
        #starting from leaf and moving to top
        #The nodes that remain after removing all the leaves are always the centroids (1 or 2 nodes), which form the root(s) of the Minimum Height Tree.
        if n == 1:
            return [0]
            
        adj_list = defaultdict(list)
        degree = [0] * n
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)
            degree[src] += 1
            degree[dst] += 1
        
        q = deque()
        #add all leaf to the deque
        for i in range(n):
            if degree[i] == 1:
                q.append(i)

        remaining_nodes = n
        #trim leaves until 2 or lower nodes remain
        while remaining_nodes > 2:
            count = len(q)
            remaining_nodes -= count
            for _ in range(count):
                leaf = q.popleft()
                for nei in adj_list[leaf]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)

        return list(q)
