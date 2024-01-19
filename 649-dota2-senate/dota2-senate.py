class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        temp=deque(senate)
        while len(temp)>1:
            a=temp.popleft()
            try:
                temp.remove('R' if a=='D' else 'D')
                temp.append(a)
            except:
                pass
        return "Radiant" if temp.pop()=="R" else "Dire"
            