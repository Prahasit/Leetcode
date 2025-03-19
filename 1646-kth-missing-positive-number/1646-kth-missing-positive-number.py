class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_set = set(arr)
        val = k + max(arr)
        num = [i for i in range(1, val + 1)]
        for i in num:
            if i not in arr_set:
                k -= 1
                if k == 0:
                    return i

        