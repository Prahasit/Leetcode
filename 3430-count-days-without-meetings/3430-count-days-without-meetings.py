class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        result = 0
        n = len(meetings)
        meetings.sort()
        cur_max = meetings[0][1]
        print(meetings)
        for i in range(1, n):
            # checking for the gap betwee nend of previous meeting and start of current meeting
            
            if meetings[i - 1][1] < meetings[i][0] and meetings[i][0]  > cur_max:
                result += meetings[i][0] - max(cur_max,meetings[i- 1][1]) - 1
                

            
            cur_max = max(cur_max,meetings[i][1])
              
        #if the days  > the last meeting add it also
        if max(cur_max,meetings[n - 1][1]) < days:
            result += days - max(cur_max,meetings[n - 1][1])

        print(result)
        # need to add the days start of meetings days if > 1
        result += meetings[0][0] - 1

        return result
