class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n = len(image), len(image[0])
        q = deque()
        visit = set()
        directions = [[0,1], [1,0], [-1, 0], [0, - 1]]
        visit.add((sr,sc))
        temp = image[sr][sc]
        
        if temp == color:
            return  image
        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or image[r][c] != temp:
                return
            
            image[r][c] = color

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            
    

        dfs(sr, sc)

        return image     


