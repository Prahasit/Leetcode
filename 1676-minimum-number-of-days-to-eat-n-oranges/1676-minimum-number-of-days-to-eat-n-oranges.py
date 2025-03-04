class Solution:
    def minDays(self, n: int) -> int:
        memo = {}
        q = deque()
        q.append(n)
        days = 0
        while q:
            temp = deque()
            for _ in range(len(q)):
                orange = q.popleft()

                if orange == 0:
                    return days
                    
                if orange not in memo:
                    memo[orange] = days

                    temp.append(orange - 1)
                    if orange % 2 == 0:
                        temp.append(orange // 2)
                    if orange % 3 == 0:
                        temp.append(orange // 3)
            q = temp
            days += 1
        
        return days

                


        