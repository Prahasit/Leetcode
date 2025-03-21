class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # convert supplies to set()
        n = len(recipes)
        result = []
        supply_set = set(supplies)
        recipe_queue = deque()
        for i in range(len(recipes)):
            recipe_queue.append(i)
        last_size = - 1

        while len(supply_set) > last_size:
            last_size = len(supply_set)
            queue_size = len(recipe_queue)

            while queue_size > 0:
                queue_size -= 1
                idx = recipe_queue.popleft()
                can_make = True
                for ingredient in ingredients[idx]:
                    if ingredient not in supply_set:
                        can_make = False
                        break
                
                if can_make:
                    supply_set.add(recipes[idx])
                    result.append(recipes[idx])
                else:
                    recipe_queue.append(idx)

        return result