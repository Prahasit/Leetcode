class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        n = len(events)
        res = events[0][0]
        prev_time = events[0][1]
        temp = events[0][1]
        for event in events[1:]:
            idx, time = event[0], event[1]
            if time - prev_time > temp:
                temp = time - prev_time
                res = idx
            elif time - prev_time == temp:
                if idx < res:
                    res = idx

            #update current_time as prev_time
            prev_time = time

        return res
            
