class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #find for +ve and -ve sign
        n = len(asteroids)
        stack = []
        for i in range(n):
            while stack and asteroids[i] < 0 and stack[-1] > 0:
                temp = stack[-1] + asteroids[i]
                if temp > 0:
                    asteroids[i] = 0

                elif temp == 0:
                    asteroids[i] = 0
                    stack.pop()
                
                else:
                    stack.pop()

            if asteroids[i]:
                stack.append(asteroids[i])
        return stack