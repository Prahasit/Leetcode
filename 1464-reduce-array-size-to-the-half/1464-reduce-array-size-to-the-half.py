class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = 0
        freq = Counter(arr)
        temp = sorted([val for num, val in freq.items()], reverse = True)
        cur = 0
        i = 0

        while cur < len(arr) // 2:
            cur += temp[i]
            count += 1
            i += 1
        return count


