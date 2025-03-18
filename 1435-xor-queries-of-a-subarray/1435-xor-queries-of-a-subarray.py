class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        prefix_xor = [0] * (len(arr) + 1) #pre computing prefix Xor to reduce time complexity
        prefix_xor[0] = arr[0]
        for i in range(len(arr)):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

        for start, end in queries:
            result.append(prefix_xor[end + 1] ^ prefix_xor[start])

        return result

