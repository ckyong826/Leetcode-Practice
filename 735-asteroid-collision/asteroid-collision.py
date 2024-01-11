class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for val in asteroids:
            while stack and stack[-1]>0>val:
                if stack[-1]<abs(val):
                    stack.pop()
                    continue
                elif stack[-1] == abs(val):
                    stack.pop()
                break
            else:
                stack.append(val)
        return stack