class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        tup=[(p,s) for p,s in zip(position,speed)]
        tup.sort(reverse=True)
        for p,s in tup:
            time = (target-p) / s
            if not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)