class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #brute force
        m, n = len(matrix), len(matrix[0])
        def binary_search(arr):
            low, high = 0, n - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
        for  i in range(m):
            if binary_search(matrix[i]):
                return True