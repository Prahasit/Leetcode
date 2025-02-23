class SeatManager:
    #without using pre- initialization
    def __init__(self, n: int):
        self.marker = 1
        self.seats = []
        
    def reserve(self) -> int:
        if len(self.seats) > 0:
            return heapq.heappop(self.seats)
        
        seat_number = self.marker
        self.marker += 1
        return seat_number

        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)