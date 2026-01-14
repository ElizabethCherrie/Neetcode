"""Task 735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). 
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.

"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            if not stack:
                stack.append(asteroids[i])
                continue

            if (stack[-1] > 0 and asteroids[i] > 0) or\
                (stack[-1] < 0 and asteroids[i] < 0):
                stack.append(asteroids[i])
                continue

            while stack and (stack[-1] > 0 and asteroids[i] < 0):
                if abs(stack[-1]) < abs(asteroids[i]):
                    stack.pop()
                elif abs(stack[-1]) == abs(asteroids[i]):
                    stack.pop()
                    break
                else:
                    break
            else:         
                stack.append(asteroids[i])

        return stack