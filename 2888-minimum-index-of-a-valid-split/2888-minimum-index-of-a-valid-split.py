class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)
        res = float('inf')
        for i in range(n):
            freq[nums[i]] += 1
        dominant = - 1
        for key, val in freq.items():
            if val > n //2:
                dominant = key
                break
        if dominant == - 1:
            return - 1

        count = 0
        for i in range(n - 1): # n - 1 as the 2nd hald cannot be empty
            if nums[i]== dominant:
                count += 1
            if count > (i + 1)// 2:
                remaining_count = freq[dominant] - count
                if remaining_count > (n - i - 1)// 2:
                    res = min(res, i)
                
        return res if res != float(inf) else - 1