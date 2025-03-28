class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        n = len(enemyEnergies)
        points = 0
        marked = [0] * n
        enemyEnergies.sort()
        if enemyEnergies[0] > currentEnergy:
            return 0
        l, r = 0, n - 1
        while l <= r:
            while marked[l] == 0 and currentEnergy >= enemyEnergies[l]:
                print(currentEnergy)
                points += currentEnergy // enemyEnergies[l]
                currentEnergy = currentEnergy % enemyEnergies[l]
             
            if marked[r] == 0:
                currentEnergy += enemyEnergies[r]
                marked[r] = 1
                r -= 1

        return points            
