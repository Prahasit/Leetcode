class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        count = 0
        sub_sum = 0
        l, r = 0, k - 1
        for i in range(l, r + 1):
            sub_sum += arr[i]
        if sub_sum // k >= threshold:
            count += 1
        print(sub_sum)
        while r < n - 1:
            sub_sum -= arr[l]
            l += 1
            r += 1
            sub_sum += arr[r]

            if sub_sum // k >= threshold:
                count += 1
        
        return count
        
