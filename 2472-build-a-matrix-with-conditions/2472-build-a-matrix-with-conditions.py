class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        #it is like topo sort like course schedule 1 should come before 2, 3 should come before 2 for the  example rowConditions = [[1,2],[3,2]]
    #1. find toposort i.e ordering in row condiotions
    #2. find ordering for col conditions
    #3.find a way to apply it in the zero matrix
    
        def toposort(edges):
            adj_list = defaultdict(list)
            indegree = [0] * (k + 1)
            q = deque()
            for src, dst in edges:
                adj_list[src].append(dst)
                indegree[dst] += 1
            for i in range(1, k + 1):
                if indegree[i] == 0:
                    q.append(i)
            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for nei in adj_list[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
            return order

        row_order = toposort(rowConditions)
        if len(row_order) != k:
            return []

        col_order = toposort(colConditions)
        if len(col_order) != k:
            return []

        #mapping the number in rows and cols with index after toposort is done
        rows, cols = {}, {}
        for i, num in enumerate(row_order):
            rows[num] = i
        for i, num in enumerate(col_order):
            cols[num] = i

        #getting the row index and col index of a number 'num'
        result_matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            r, c = rows[num], cols[num]
            result_matrix[r][c] = num

        return result_matrix


    