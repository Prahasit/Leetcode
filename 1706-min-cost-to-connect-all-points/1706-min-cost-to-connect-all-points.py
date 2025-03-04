class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #it is similar to MST after finding the manhattan distance
        n = len(points)
        total_dist = 0
        visit = [False] * n
        dist = [10000000] * n
        edges, node = 0, 0

        while edges < n - 1:
            visit[node] = True
            nextNode = - 1 #for every loop initilize it to -1
            for i in range(n):
                if visit[i]:
                    continue
                cur_dist = abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])
                dist[i] = min(dist[i], cur_dist)

                if nextNode == - 1 or dist[i] < dist[nextNode]:
                    nextNode = i
                
            # after loop for every index we get the minimum dist and move the node to that element
            total_dist += dist[nextNode]
            node = nextNode # as this index dist is minimim update the node to this node and find from here
            edges += 1
        
        return total_dist
