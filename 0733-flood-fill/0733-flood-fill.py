class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n = len(image), len(image[0])
        q = deque()
        visit = set()
        directions = [[0,1], [1,0], [-1, 0], [0, - 1]]
        visit.add((sr,sc))
        q.append((sr,sc))

        temp = image[sr][sc]
        while q: # need to level wise
            for _ in range(len(q)):
                r, c = q.popleft()
                image[r][c] = color
                for dr,dc in directions:
                    row, col = dr+r, dc +c
                    if 0<= row < m and 0<= col < n and image[row][col] == temp:
                        if (row, col) not in visit:
                            q.append((row, col))
                            visit.add((row, col))

        return image
                            


