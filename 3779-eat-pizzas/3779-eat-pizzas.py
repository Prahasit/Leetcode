class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        n = len(pizzas)
        total_sum = 0
        days = n // 4
        even_days  = days // 2
        odd_days = days - even_days

        temp = [val for i, val in enumerate(pizzas)]
        sorted_pizza = sorted(temp)
        print(sorted_pizza)
        print(odd_days)
        print(even_days)
        l, r  = 0, n - 1
        while odd_days > 0:
            total_sum += sorted_pizza[r]
            
            l += 3
            r -= 1
            odd_days -= 1
 
        while even_days > 0:
            total_sum += sorted_pizza[r - 1]
            l += 2
            r -= 2
            even_days -= 1
        
        return total_sum