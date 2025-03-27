class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # check ith element of s and t until it <= cost
        #if > cost reduce from the l= 0 with l += 1

        n = len(s)
        l, r = 0, 0
        max_len = 0
        cur_cost = 0

        while r < n:
            cur_cost += abs(ord(s[r]) - ord(t[r]))
            while cur_cost > maxCost:
                cur_cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            
            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len


