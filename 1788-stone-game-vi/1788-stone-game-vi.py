class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        #If Alice and Bob both want to maximize their own scores, they should prioritize picking stones that have the highest combined value.

        n = len(aliceValues)
        stones = [(- (aliceValues[i] + bobValues[i]), aliceValues[i], bobValues[i]) for i in range(n)]
        heapq.heapify(stones)

        alice, bob = 0, 0
        start = 0

        while stones:
            _, a, b = heapq.heappop(stones)
            if start % 2 == 0:
                alice += a
            else:
                bob += b
            start += 1
            
        if alice == bob:
            return 0
        elif alice > bob:
            return 1
        else:
            return -1
