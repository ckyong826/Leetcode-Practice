class Solution:
    def minOperations(self, s: str) -> int:
        temp1= bool(int(s[0]))
        temp2= not bool(int(s[0]))
        count1,count2=0,1
        for i in range(1,len(s)):
            if temp1 !=bool(int(s[i])):
                temp1=bool(int(s[i]))
            else:
                count1+=1
                temp1=not bool(int(s[i]))
            if temp2 !=bool(int(s[i])):
                temp2=bool(int(s[i]))
            else:
                count2+=1
                temp2=not bool(int(s[i]))
        return min(count1,count2)


            