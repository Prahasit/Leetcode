class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        # a = 1, b = 0
        n = len(energyDrinkA)
        memo = {}

        def solve(i, drinkA):
            if i >= n:
                return 0

            if (i, drinkA) in memo:
                return memo[(i, drinkA)]
            if drinkA:
                no_changeA = energyDrinkA[i] + solve(i+ 1, True)
                changeA = solve(i + 1, False) 
                memo[(i, drinkA)] =  max(no_changeA, changeA)
                 
            else:
                no_changeB = energyDrinkB[i] +solve(i+ 1, False)
                changeB = solve(i + 1, True) 

                memo[(i, drinkA)] = max(no_changeB, changeB)

            return memo[(i, drinkA)]

        return max(solve(0, True), solve(0, False))