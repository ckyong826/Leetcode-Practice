class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        temp=[]
        temp.extend(s[:k])
        count=0
        for w in temp:
            if w in "aeiou":
                count+=1
        maxCount=count
        for i in range(len(s)-k):
            temp.append(s[i+k])
            a=temp.pop(0)
            if a in "aeiou":
                count-=1
            if s[i+k] in "aeiou":
                count+=1
            maxCount=max(maxCount,count)
        return maxCount