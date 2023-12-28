class Solution:
    def compress(self, chars: List[str]) -> int:
        temp=[]
        j=0
        for i in range(len(chars)):
            if i==0:
                temp.append(chars[i])
            if chars[i]!=chars[j]:
                count=i-j
                if count>1:
                    temp.extend(list(str(count)))
                temp.append(chars[i])
                j=i
            elif i==len(chars)-1:
                count=i-j+1
                if count>1:
                    temp.extend(list(str(count)))
        chars.clear()
        chars.extend(temp)
        
