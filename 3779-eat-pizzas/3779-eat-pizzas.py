class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        #odd takes largest element, even takes 2nd largest element.
        #so first calculating odd first
        weight = 0
        days = len(pizzas)//4
        pizzas.sort()
        r = len(pizzas) - 1
        for i in range(1, days + 1, 2):
            weight += pizzas[r] #largest
            r -= 1
        
        for i in range(2, days + 1, 2 ):
            weight += pizzas[r - 1] #second largest
            r -= 2
        return weight


