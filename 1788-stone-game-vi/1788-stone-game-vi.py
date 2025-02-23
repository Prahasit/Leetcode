class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        #If Alice and Bob both want to maximize their own scores, they should prioritize picking stones that have the highest combined value.

        stones = sorted(zip(aliceValues, bobValues), key=lambda x: -(x[0] + x[1]))
        
        alice, bob = 0, 0
        for i, (a, b) in enumerate(stones):
            if i % 2 == 0:  # Alice's turn
                alice += a
            else:           # Bob's turn
                bob += b
        if alice == bob:
            return 0
        elif alice > bob:
            return 1
        else:
            return -1
