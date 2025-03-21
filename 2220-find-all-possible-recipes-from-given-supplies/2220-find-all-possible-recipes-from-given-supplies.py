class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # convert supplies to set()
        n = len(recipes)
        result = []
        supply_set = set(supplies)
        recipe_queue = deque()
        adj_list = defaultdict(list)
        indegree = [0] * n
        recipe_to_index = {recipe: idx for idx, recipe in enumerate(recipes)}
        for idx, ingredient_list in enumerate(ingredients):
            for ingredient in ingredient_list:
                if ingredient not in supply_set:
                    indegree[idx] += 1
                    adj_list[ingredient].append(recipes[idx])

        for idx, count in enumerate(indegree):
            if count == 0:
                recipe_queue.append(idx)

        while recipe_queue:
            idx = recipe_queue.popleft()
            recipe = recipes[idx]
            result.append(recipe)

            for nei in adj_list[recipe]:
                indegree[recipe_to_index[nei]] -= 1
                if indegree[recipe_to_index[nei]] == 0:
                    recipe_queue.append(recipe_to_index[nei])
        return result