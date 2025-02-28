class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #for everytime increase depth by 1. 
        #if going up decreae depth by 1
        
        if numRows == 1 or numRows > len(s):
            return s
        
        idx, depth = 0, 1
        rows = [[] for _ in range(numRows)]

        for i in s:
            rows[idx].append(i)
            if idx == 0:
                depth = 1
            elif idx == numRows - 1:
                depth = -1
            idx += depth

        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        return ''.join(rows)

    
        