class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # it comes down to [-x, +x, -y, +y] as if we take example x = 3, y = 5, if we fill y = 5 then we have options to empty y i.e - 5 or fill 3 i. e +3 or also transfer from y to x i.e 5 - 3 i.e -3 for fill i.e + 5
        if target > x + y:
            return False
        q = deque()
        q.append(0)
        visit = set()
        operations = [-x, +x, -y, +y]
        while q:
            cur = q.popleft()
            for temp in operations:
                tot = cur + temp
                if tot == target:
                    return True
                if tot not in visit and 0 <= tot <= x + y :
                    visit.add(tot)
                    q.append(tot)
        return False

