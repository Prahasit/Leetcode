class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        hopOnOff = []
        for count, start, end in trips:
            hopOnOff.append((start, count))
            hopOnOff.append((end, -count))

        hopOnOff.sort()

        inCar = 0
        for destination, passangers in hopOnOff:
            inCar += passangers
            if inCar > capacity:
                return False
        return True