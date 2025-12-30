class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        res = []
        res.append(intervals[0])
        for start, end in intervals[1:]:
            new_end = res[-1][1]

            if start <= new_end:
                res[-1][1] = max(end, new_end)

            else:
                res.append([start, end])


        return res